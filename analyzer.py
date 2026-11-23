import re
from collections import Counter

# Read the file we saved earlier
with open("failures.txt") as f:
    lines = f.readlines()

users = Counter()
programs = Counter()
total = 0

for line in lines:
    # Only keep real login failures
    if "authentication failure" not in line:
        continue

    total += 1

    # Find the user name (the space before "user=" skips "ruser=")
    user_match = re.search(r"\suser=(\S+)", line)
    if user_match:
        users[user_match.group(1)] += 1

    # Find the program name (su, gdm-password, sshd...)
    prog_match = re.search(r"kali ([^\s\[\]:]+)", line)
    if prog_match:
        programs[prog_match.group(1)] += 1

print("=== Failed Login Report ===")
print("Total failed logins:", total)

print("\nTop targeted users:")
for user, count in users.most_common(5):
    print(" ", user, "-", count)

print("\nWhich programs reported failures:")
for prog, count in programs.most_common(5):
    print(" ", prog, "-", count)

if total >= 5:
    print("\nALERT: 5 or more failed logins found. Possible brute-force attempt.")
