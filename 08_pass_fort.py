import os
import base64

# File where all encrypted credentials are stored
VAULT_FILE = "vault.txt"


def encode(text):
    """
    Encode plain text to base64 string.
    This provides a very light obfuscation (NOT secure encryption).
    """
    return base64.b64encode(text.encode()).decode()


def decode(text):
    """
    Decode base64 string back to plain text.
    """
    return base64.b64decode(text.encode()).decode()


def add_credential():
    """
    Prompt user for website, username, and password.
    Evaluate password strength, then append the encoded credential to vault.txt.
    """
    website = input("Enter the website url: ").strip()
    username = input("Enter the username: ").strip()
    password = input("Enter the password: ").strip()

    # Show user how strong their password is
    strength = password_strength(password)
    print(f"Password Strength: {strength}")

    # Combine fields with a delimiter and encode
    unsecure_credential = f"{website} || {username} || {password}"
    secure_credential = encode(unsecure_credential)

    # Append encoded line to vault file
    with open(VAULT_FILE, "a", encoding="utf-8") as f:
        f.write(secure_credential + "\n")
        print("✅ Credential added successfully.")


def password_strength(password):
    """
    Return a qualitative strength label for the given password.
    Checks length, upper/lower cases, digits, and special characters.
    """
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    # Count how many criteria are satisfied (0-5)
    strength = sum([length >= 8, has_upper, has_lower, has_digit, has_special])

    # Map score to label (cap at index 3)
    return ["Weak", "Medium", "Strong", "Very Strong"][min(strength, 3)]


def view_credentials():
    """
    Read vault file, decode each line, and print credentials in a friendly format.
    """
    # Early exit if vault does not exist yet
    if not os.path.exists(VAULT_FILE):
        print("No credentials found.")
        return

    # Process each stored line
    with open(VAULT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            secure_credential = line.strip()
            decoded_credential = decode(secure_credential)

            # Split on delimiter used during storage
            website, username, password = decoded_credential.split(" || ")
            print(
                f"🌐 Website: {website} | 👤 Username: {username} | 🔑 Password: {password}"
            )


def update_password():
    """
    Allow user to update the password for an existing website entry.
    Keeps username and website unchanged.
    """
    website = input("Enter the website url to update the password: ").strip()

    # Ensure vault exists
    if not os.path.exists(VAULT_FILE):
        print("No credentials found.")
        return

    # Read all lines into memory
    lines = []
    with open(VAULT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Look for matching website (case-insensitive)
    updated = False
    for i, line in enumerate(lines):
        decoded_credential = decode(line.strip())
        url, username, password = decoded_credential.split(" || ")
        if website.lower() == url.strip().lower():
            new_password = input("Enter the new password: ").strip()
            # Show strength of new password
            strength = password_strength(new_password)
            print(f"Password Strength: {strength}")
            # Rebuild credential with new password and encode
            unsecure_credential = f"{url} || {username} || {new_password}"
            lines[i] = encode(unsecure_credential) + "\n"
            updated = True
            print("✅ Password updated successfully.")

    # Write back all lines (modified or not)
    if updated:
        with open(VAULT_FILE, "w", encoding="utf-8") as f:
            f.writelines(lines)
    else:
        print("Website not found.")


def main():
    """
    Simple text menu loop for the credential manager.
    Choices: Add, View, Update, Exit.
    """
    while True:
        print("-" * 20 + "Offline Credential Manager 🔐" + "-" * 20)
        print("1. Add Credential")
        print("2. View All Credentials")
        print("3. Update Password")
        print("4. Exit")

        option = input("Enter your choice (1-4): ").strip()

        match option:
            case "1":
                add_credential()
            case "2":
                view_credentials()
            case "3":
                update_password()
            case "4":
                print("Close the Credential Manager.")
                break
            case _:
                print("Invalid choice. Please enter a number between 1 and 4.")


# Run the program only when executed directly (not imported)
if __name__ == "__main__":
    main()
