import sys
import csv
import json
import re
from collections import Counter

def main():
    """Main function - entry point of the program."""

    if len(sys.argv) < 2:
        print("Usage: python project.py <logfile>")
        print("Example: python project.py auth.log")
        sys.exit(1)

    log_file = sys.argv[1]

    try:

        logs = load_log(log_file)


        failed_count = count_failed(logs)
        successful_count = count_successful(logs)
        top_ips = find_top_ips(logs)
        targeted_users = find_targeted_users(logs)
        risk_level = calculate_risk(failed_count)

        brute_force_ips = detect_brute_force(logs)

        # report
        print_report(failed_count, successful_count, top_ips,
                    targeted_users, risk_level, brute_force_ips)

        # Export to CSV if user wants
        if len(sys.argv) > 2 and sys.argv[2] == "--export-csv":
            export_csv(failed_count, successful_count, top_ips,
                      targeted_users, risk_level, brute_force_ips, "report.csv")
            print("\n Report exported to report.csv")

        # Export to JSON if user wants
        if len(sys.argv) > 2 and sys.argv[2] == "--export-json":
            export_json(failed_count, successful_count, top_ips,
                       targeted_users, risk_level, brute_force_ips, "report.json")
            print("\n Report exported to report.json")

    except FileNotFoundError:
        print(f"Error: File '{log_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def load_log(filename):
    """Load and parse the log file."""
    logs = []


    pattern = r'(?:Failed password|Accepted password) for (?:invalid user )?(\S+) from (\S+)'

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()


                match = re.search(pattern, line)
                if match:
                    username = match.group(1)
                    ip = match.group(2)

                    if "Failed password" in line:
                        status = "failed"
                    else:
                        status = "successful"

                    log_entry = {
                        "username": username,
                        "ip": ip,
                        "status": status
                    }
                    logs.append(log_entry)


    except FileNotFoundError:
        raise FileNotFoundError(f"Log file '{filename}' not found.")

    return logs

def count_failed(logs):
    """Count total failed login attempts using list comprehension."""
    return sum(1 for log in logs if log["status"] == "failed")

def count_successful(logs):
    """Count total successful login attempts using list comprehension."""
    return sum(1 for log in logs if log["status"] == "successful")

def find_top_ips(logs):
    """Find top IPs with most failed attempts."""

    failed_ips = [log["ip"] for log in logs if log["status"] == "failed"]


    ip_counts = Counter(failed_ips)

    top_ips = ip_counts.most_common(5)
    return top_ips

def find_targeted_users(logs):
    """Find usernames that were targeted in failed attempts."""

    users = {log["username"] for log in logs if log["status"] == "failed"}
    return sorted(list(users))

def calculate_risk(failed_count):
    """Calculate risk level based on number of failed attempts."""
    if failed_count > 20:
        return "CRITICAL"
    elif failed_count > 10:
        return "HIGH"
    elif failed_count > 5:
        return "MEDIUM"
    else:
        return "LOW"

def detect_brute_force(logs, threshold=5):
    """Detect possible brute force attacks (IPs with many failed attempts)."""

    ip_counts = Counter()
    for log in logs:
        if log["status"] == "failed":
            ip_counts[log["ip"]] += 1


    suspicious_ips = []
    for ip, count in ip_counts.items():
        if count >= threshold:
            suspicious_ips.append({"ip": ip, "attempts": count})


    suspicious_ips.sort(key=lambda x: x["attempts"], reverse=True)
    return suspicious_ips

def print_report(failed, successful, top_ips, users, risk, brute_force_ips):
    """Print the security report with brute force detection."""
    print("\n" + "=" * 50)
    print("SECURITY REPORT")
    print("=" * 50)

    print(f"\nFailed logins: {failed}")
    print(f"Successful logins: {successful}")

    if top_ips:
        print("\nTop attacker IPs")
        for ip, count in top_ips:
            print(f"  {ip}  ({count})")

    if users:
        print("\nTargeted usernames")
        for user in users:
            print(f"  {user}")


    if brute_force_ips:
        print("\nPossible Brute Force Attacks Detected:")
        for entry in brute_force_ips:
            print(f" {entry['ip']} - {entry['attempts']} failed attempts")
    else:
        print("\nNo brute force attacks detected")


    if risk == "CRITICAL":
        risk_display = "CRITICAL"
    elif risk == "HIGH":
        risk_display = "HIGH"
    elif risk == "MEDIUM":
        risk_display = "MEDIUM"
    else:
        risk_display = "LOW"

    print(f"\nRisk Level: {risk_display}")
    print("=" * 50 + "\n")

def export_csv(failed, successful, top_ips, users, risk, brute_force_ips, filename):
    """Export report to CSV."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)


        writer.writerow(["Metric", "Value"])
        writer.writerow(["Failed logins", failed])
        writer.writerow(["Successful logins", successful])
        writer.writerow(["Risk Level", risk])
        writer.writerow([])


        writer.writerow(["IP Address", "Attempts"])
        for ip, count in top_ips:
            writer.writerow([ip, count])
        writer.writerow([])


        writer.writerow(["Targeted Usernames"])
        for user in users:
            writer.writerow([user])
        writer.writerow([])


        if brute_force_ips:
            writer.writerow(["Brute Force Detected", "Attempts"])
            for entry in brute_force_ips:
                writer.writerow([entry["ip"], entry["attempts"]])

def export_json(failed, successful, top_ips, users, risk, brute_force_ips, filename):
    """Export report to JSON."""
    data = {
        "failed_logins": failed,
        "successful_logins": successful,
        "risk_level": risk,
        "top_attacking_ips": [
            {"ip": ip, "attempts": count}
            for ip, count in top_ips
        ],
        "targeted_users": users,
        "brute_force_detected": [
            {"ip": entry["ip"], "attempts": entry["attempts"]}
            for entry in brute_force_ips
        ]
    }

    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)

if __name__ == "__main__":
    main()
