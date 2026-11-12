
from urllib.parse import quote

print("Enter LeetCode profile IDs or names (one per line).")
print("Type DONE when finished:\n")

profiles = []

while True:
    profile = input()

    if profile.strip().upper() == "DONE":
        break

    profiles.append(profile)

print("\nGenerated LeetCode Profile URLs:\n")

for profile in profiles:

    # Preserve empty lines
    if not profile.strip():
        print()
        continue

    profile = profile.strip()

    # If already a full LeetCode profile URL
    if profile.startswith("https://leetcode.com/u/"):
        print(profile.rstrip("/\\") + "/")
        continue

    # Remove leading @ symbols
    profile = profile.lstrip("@")

    # Remove trailing / and \ symbols
    profile = profile.rstrip("/\\")

    # Preserve names containing spaces
    if " " in profile:
        print(profile)
        continue

    # Generate LeetCode profile URL
    if profile:
        print(f"https://leetcode.com/u/{quote(profile, safe='')}/")
    else:
        print()
