# Incident Report: Repeated Failed Logins

**Analyst:** Sneha
**Date of analysis:** 23 November 2026
**System:** Kali Linux workstation (single host)
**Tool used:** Custom Python log analyzer (analyzer.py)

## 1. Summary
The log analyzer detected 6 failed authentication attempts in the system journal within one hour. Five were against the account `nobody` using the `su` command. One was a failed login at the graphical login screen (gdm-password) for the user `sneha`. The alert threshold of 5 failures was reached.

## 2. Timeline
| Time (approx.) | Event |
|---|---|
| 02:42 | First failed `su` attempt against user `nobody` |
| 02:42 to 02:45 | Further failed `su` attempts (5 in total) |
| 06:22 | One failed login at the login screen for user `sneha` |
| After collection | Analyzer ran and raised an ALERT |

(Adjust these times to match your own failures.txt. You can check them with `cat failures.txt`.)

## 3. Indicators
- **Targeted accounts:** nobody (5 attempts), sneha (1 attempt)
- **Reporting programs:** su (5), gdm-password (1)
- **Source IP address:** none. All attempts were local, so no remote attacker is involved.

## 4. How it was detected
A Python script reads failed-login lines from `journalctl`, extracts the username and program with regular expressions, counts them, and raises an alert at 5 or more failures.

## 5. Assessment
The `su` failures were created by me on purpose to test the analyzer, so this was a controlled test, not a real attack. The single `gdm-password` failure was most likely a mistyped password by the legitimate user. In a real environment, five failed `su` attempts against a service account like `nobody` in a short time would deserve investigation.

## 6. Recommendations
- Lock the account or require a delay after repeated failures (for example with `pam_faillock`)
- Check who had physical or remote access at the time
- Restrict `su` and `sudo` to trusted users only
- Extend the analyzer to track source IP addresses and time windows
