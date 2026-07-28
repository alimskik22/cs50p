import pytest
import tempfile
import os
from project import load_log, count_failed, count_successful, find_top_ips, find_targeted_users, calculate_risk, detect_brute_force


SAMPLE_LOGS = [
    'Jul 17 09:14 sshd[2134]: Failed password for root from 185.220.101.5',
    'Jul 17 09:14 sshd[2135]: Failed password for root from 185.220.101.5',
    'Jul 17 09:15 sshd[2136]: Accepted password for alima from 192.168.1.10',
    'Jul 17 09:16 sshd[2137]: Failed password for admin from 91.92.15.10',
    'Jul 17 09:17 sshd[2138]: Failed password for root from 185.220.101.5',
    'Jul 17 09:18 sshd[2139]: Failed password for admin from 185.220.101.5',
]


SAMPLE_WITH_INVALID = [
    'Jul 17 09:14 sshd[2134]: Failed password for invalid user root from 185.220.101.5',
    'Jul 17 09:15 sshd[2136]: Accepted password for alima from 192.168.1.10',
]

def create_test_log(content):
    """Helper function to create a temporary log file."""
    temp = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.log')
    temp.write('\n'.join(content))
    temp.close()
    return temp.name

def cleanup_test_file(filename):
    """Helper function to delete temporary test files."""
    try:
        os.unlink(filename)
    except:
        pass

def test_load_log():
    """Test loading and parsing log files."""
    log_file = create_test_log(SAMPLE_LOGS)
    logs = load_log(log_file)
    cleanup_test_file(log_file)

    assert len(logs) == 6
    assert logs[0]["username"] == "root"
    assert logs[0]["ip"] == "185.220.101.5"
    assert logs[0]["status"] == "failed"

def test_load_log_with_invalid_user():
    """Test loading logs with 'invalid user' entries."""
    log_file = create_test_log(SAMPLE_WITH_INVALID)
    logs = load_log(log_file)
    cleanup_test_file(log_file)

    assert len(logs) == 2
    assert logs[0]["username"] == "root"
    assert logs[0]["ip"] == "185.220.101.5"
    assert logs[0]["status"] == "failed"

def test_load_log_file_not_found():
    """Test loading a non-existent log file."""
    with pytest.raises(FileNotFoundError):
        load_log("nonexistent_file.log")

def test_load_log_malformed():
    """Test loading malformed log entries."""
    malformed = [
        "This is not a valid log line",
        "Jul 17 09:14 sshd[2134]: Random message",
    ]
    log_file = create_test_log(malformed)
    logs = load_log(log_file)
    cleanup_test_file(log_file)


    assert len(logs) == 0

def test_count_failed():
    """Test counting failed login attempts."""
    log_file = create_test_log(SAMPLE_LOGS)
    logs = load_log(log_file)
    cleanup_test_file(log_file)


    assert count_failed(logs) == 5

def test_count_failed_empty():
    """Test counting failed attempts with no logs."""
    log_file = create_test_log([])
    logs = load_log(log_file)
    cleanup_test_file(log_file)
    assert count_failed(logs) == 0

def test_count_failed_no_failures():
    """Test when there are no failed attempts."""
    success_only = [
        'Jul 17 09:15 sshd[2136]: Accepted password for alima from 192.168.1.10',
        'Jul 17 09:16 sshd[2137]: Accepted password for john from 192.168.1.10',
    ]
    log_file = create_test_log(success_only)
    logs = load_log(log_file)
    cleanup_test_file(log_file)
    assert count_failed(logs) == 0

def test_count_successful():
    """Test counting successful login attempts."""
    log_file = create_test_log(SAMPLE_LOGS)
    logs = load_log(log_file)
    cleanup_test_file(log_file)

    assert count_successful(logs) == 1

def test_find_top_ips():
    """Test finding top attacking IPs."""
    log_file = create_test_log(SAMPLE_LOGS)
    logs = load_log(log_file)
    cleanup_test_file(log_file)

    top_ips = find_top_ips(logs)


    assert len(top_ips) == 2


    assert top_ips[0][0] == '185.220.101.5'
    assert top_ips[0][1] == 4


    assert top_ips[1][0] == '91.92.15.10'
    assert top_ips[1][1] == 1

def test_find_top_ips_no_failures():
    """Test finding top IPs when there are no failed attempts."""
    success_only = [
        'Jul 17 09:15 sshd[2136]: Accepted password for alima from 192.168.1.10',
        'Jul 17 09:16 sshd[2137]: Accepted password for john from 192.168.1.10',
    ]
    log_file = create_test_log(success_only)
    logs = load_log(log_file)
    cleanup_test_file(log_file)

    top_ips = find_top_ips(logs)
    assert len(top_ips) == 0

def test_find_targeted_users():
    """Test finding targeted usernames."""
    log_file = create_test_log(SAMPLE_LOGS)
    logs = load_log(log_file)
    cleanup_test_file(log_file)

    users = find_targeted_users(logs)
    assert users == ['admin', 'root']

def test_calculate_risk():
    """Test risk calculation with different thresholds."""
    assert calculate_risk(25) == "CRITICAL"
    assert calculate_risk(15) == "HIGH"
    assert calculate_risk(8) == "MEDIUM"
    assert calculate_risk(3) == "LOW"

def test_detect_brute_force():
    """Test brute force detection."""
    brute_logs = []
    for i in range(10):
        brute_logs.append(
            f'Jul 17 09:{i:02d} sshd[2134]: Failed password for root from 185.220.101.5'
        )

    log_file = create_test_log(brute_logs)
    logs = load_log(log_file)
    cleanup_test_file(log_file)

    brute_force = detect_brute_force(logs, threshold=5)
    assert len(brute_force) == 1
    assert brute_force[0]["ip"] == "185.220.101.5"
    assert brute_force[0]["attempts"] == 10

def test_detect_brute_force_threshold():
    """Test brute force detection with custom threshold."""
    brute_logs = []
    for i in range(3):
        brute_logs.append(
            f'Jul 17 09:{i:02d} sshd[2134]: Failed password for root from 185.220.101.5'
        )

    log_file = create_test_log(brute_logs)
    logs = load_log(log_file)
    cleanup_test_file(log_file)


    brute_force = detect_brute_force(logs, threshold=5)
    assert len(brute_force) == 0


    brute_force = detect_brute_force(logs, threshold=3)
    assert len(brute_force) == 1

def test_detect_brute_force_multiple_ips():
    """Test brute force detection with multiple IPs."""
    logs_data = []
    for i in range(8):
        logs_data.append(
            f'Jul 17 09:{i:02d} sshd[2134]: Failed password for root from 185.220.101.5'
        )
    for i in range(6):
        logs_data.append(
            f'Jul 17 09:{i:02d} sshd[2134]: Failed password for admin from 192.168.1.10'
        )

    log_file = create_test_log(logs_data)
    logs = load_log(log_file)
    cleanup_test_file(log_file)

    brute_force = detect_brute_force(logs, threshold=5)
    assert len(brute_force) == 2
    assert brute_force[0]["ip"] == "185.220.101.5"
    assert brute_force[0]["attempts"] == 8
    assert brute_force[1]["ip"] == "192.168.1.10"
    assert brute_force[1]["attempts"] == 6


