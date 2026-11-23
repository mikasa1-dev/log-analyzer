# Log Analyzer: Failed Login Detector

A small Python tool that reads Linux system logs, finds repeated failed logins, and raises an alert when it sees a possible brute-force attempt.

## What it does
- Reads failed-login lines from the system journal
- Counts failures per user and per program (su, gdm-password, sshd...)
- Prints an ALERT when there are 5 or more failures

## Tools used
Python 3, Kali Linux, journalctl

## How to run
1. Export the failed-login lines from the system log:
   `sudo journalctl --since "1 hour ago" --no-pager | grep -i "fail" > failures.txt`
2. Run the analyzer:
   `python3 analyzer.py`

## Example output
![Report screenshot](report.png)

## What I learned
- How Linux records authentication events
- How to extract data from log lines using regular expressions
- A bug I fixed: `ruser=` was matching `user=`, so I changed the pattern to require a space before `user=`

## Limitations
- It is a small script, not a SIEM
- It does not read IP addresses yet

## Future improvements
- Detect failed SSH logins with source IP addresses
- Add a time window (for example, 5 failures within 1 minute)
- Export the report to a file
