
from urllib.parse import quote

print("Enter CodeChef profile IDs or names (one per line).")
print("Type DONE when finished:\n")

profiles = []

while True:
    profile = input()

    if profile.strip().upper() == "DONE":
        break

    profiles.append(profile)

print("\nGenerated CodeChef Profile URLs:\n")

for profile in profiles:

    # Preserve empty lines
    if not profile.strip():
        print()
        continue

    profile = profile.strip()

    # If already a full CodeChef profile URL
    if profile.startswith("https://www.codechef.com/users/"):
        print(profile.rstrip("/\\"))
        continue

    # Remove leading @ symbols
    profile = profile.lstrip("@")

    # Remove trailing / and \ symbols
    profile = profile.rstrip("/\\")

    # Preserve names containing spaces
    if " " in profile:
        print(profile)
        continue

    # Generate CodeChef profile URL
    if profile:
        print(f"https://www.codechef.com/users/{quote(profile, safe='')}")
    else:
        print()
