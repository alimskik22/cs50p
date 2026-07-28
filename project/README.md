# LogSentry - Linux Log Analyzer

#### Video Demo: <https://youtu.be/5Dkap_TZs7c?si=ejd2mubN9tnw8Q3a>

#### Description:

LogSentry is a Python-based security analysis tool designed to parse and analyze Linux authentication logs, specifically focusing on SSH login attempts. The tool was inspired by the need to quickly assess system security by identifying patterns of failed logins, tracking suspicious IP addresses, and detecting potential brute-force attacks.

## Project Overview

The program reads authentication log files (typically `/var/log/auth.log` or similar) and generates comprehensive security reports. It extracts meaningful information from raw log entries, counts successful and failed login attempts, identifies the most aggressive attacking IP addresses, and calculates an overall risk score based on the observed patterns. The tool also includes brute-force attack detection, which flags IP addresses that exceed a configurable threshold of failed attempts.

The project consists of two main files: `project.py` containing all the analysis logic, and `test_project.py` containing comprehensive unit tests using pytest. This separation of concerns follows good software engineering practices by keeping the implementation and testing code distinct.

## File Structure and Functions

### project.py

The main program file contains all the core functionality organized into clearly defined functions:

**`main()`** - The entry point that handles command-line arguments, orchestrates the analysis workflow, and manages optional export features. It checks for proper usage, handles errors gracefully, and displays the final report. This function demonstrates proper error handling with try-except blocks and provides clear user feedback.

**`load_log(filename)`** - Parses the log file using regular expressions to extract username and IP address information. I chose regex over simple string splitting because real-world logs can vary in format, especially with "invalid user" entries. The pattern `(?:Failed password|Accepted password) for (?:invalid user )?(\S+) from (\S+)` robustly handles both standard and non-standard log formats. This was one of the most important design decisions because proper parsing is critical for accurate analysis.

**`count_failed(logs)`** and **`count_successful(logs)`** - Use list comprehensions to efficiently count login attempts. I initially wrote these as for loops but refactored to comprehensions for cleaner, more Pythonic code that's easier to read once you understand the syntax. This demonstrates my growing comfort with Python's functional programming features.

**`find_top_ips(logs)`** - Employs Python's `Counter` from the collections module to identify the most frequent attacking IP addresses. This is more elegant than manually maintaining a dictionary of counts and demonstrates using Python's standard library effectively. The function returns the top 5 attacking IPs, which is a reasonable number for most security reports.

**`find_targeted_users(logs)`** - Extracts unique usernames targeted in failed attempts. I used a set comprehension to eliminate duplicates automatically, then sorted the results alphabetically for consistent output. This approach is both efficient and readable.

**`calculate_risk(failed_count)`** - Implements a simple but effective risk scoring system based on the number of failed attempts. The thresholds (CRITICAL >20, HIGH >10, MEDIUM >5, LOW ≤5) were chosen based on common security best practices and typical attack patterns observed in real-world scenarios. I made the design decision to keep this function focused solely on the count , rather than passing the entire logs list, to avoid unnecessary recomputation.

**`detect_brute_force(logs, threshold=5)`** - Flags IP addresses with excessive failed attempts. The default threshold of 5 attempts was selected because it catches dictionary attacks while minimizing false positives from legitimate users who might mistype their password a few times. This function adds significant value by identifying active attacks rather than just reporting statistics.

**`print_report(...)`** - This function separates presentation logic from analysis logic, making it easier to modify the output format later if needed.

**`export_csv(...)`** and **`export_json(...)`** - Provide structured data export capabilities for integration with other tools or further analysis. I included both formats because CSV is widely used for spreadsheets and data analysis tools, while JSON is more suitable for programmatic consumption and API integration.

### test_project.py

The test file contains comprehensive unit tests for all core functionality using pytest.

Each test uses temporary files created with `tempfile.NamedTemporaryFile()` to ensure tests are isolated and don't affect the filesystem. I also included cleanup functions to remove temporary files after tests complete.

## Design Decisions

One of the key design decisions was keeping the entire project in a single file rather than splitting into multiple modules.

Another important decision was using regular expressions for parsing rather than simple string splitting. While regex can be harder to read, it's much more robust and handles edge cases that would break simpler parsing approaches. The regex pattern I chose handles both standard log entries and entries with "invalid user" in them, which is a common format in real SSH logs.

I also decided to implement brute force detection as a separate function rather than integrating it into the main analysis. This separation allows users to easily modify the detection threshold and makes the code more maintainable.

## Installation and Setup

To install and run LogSentry:

1. Clone or download the project files to your local machine
2. No external dependencies are required for running the program (it uses only Python's standard library)
3. Run the program with a log file:
```bash
python project.py sample.log
```

## Usage Examples

Basic usage to analyze a log file:

```bash
python project.py sample.log
```

Export results to CSV:

```bash
python project.py sample.log --export-csv
```

Export results to JSON:

```bash
python project.py sample.log --export-json
```

## Running Tests

To run the test suite, you'll need to install `pytest` first:

```bash
pip install pytest
```

Then run the tests:

```bash
pytest test_project.py
```

## Sample Output

When you run the program on a sample log file, you'll see output similar to:

```text
==================================================
SECURITY REPORT
==================================================

Failed logins: 11
Successful logins: 2

Top attacker IPs
  185.220.101.5  (8)
  91.92.15.10    (3)

Targeted usernames
  admin
  guest
  root
  test

Possible Brute Force Attacks Detected:
  185.220.101.5 - 8 failed attempts

Risk Level: HIGH
==================================================
```

## Acknowledgments

- CS50x and CS50P for teaching the fundamentals of Python programming.
- The open-source community for providing excellent tools like `pytest`.
