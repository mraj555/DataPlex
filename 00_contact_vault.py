import csv
import os

# Name of the CSV file used to store contact data
FILENAME = "contacts.csv"

# If the contacts file doesn't exist, create it and write the header row
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # Write column headers: Name, Mobile No., Email ID
        writer.writerow(["Name", "Mobile No.", "Email ID"])


def add_contact():
    """Prompt user for contact details and add to CSV if name is unique."""
    name = input("Name: ")
    mobile = input("Mobile No.: ")
    email = input("Email ID: ")

    # Open file in read mode to check for duplicate names
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Case-insensitive comparison to avoid duplicate names
            if name.lower() == row["Name"].lower():
                print("Contact already exists.")
                return

        # If no duplicate found, append new contact to the file
        with open(FILENAME, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([name, mobile, email])
            print("Contact added successfully.")


def view_contacts():
    """Display all contacts stored in the CSV file."""
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

        # Check if only header row exists (no actual contacts)
        if len(rows) < 1:
            print("No contacts found.")
        else:
            # Print each contact row in a readable format
            for row in rows:
                print(f"{row[0]} | {row[1]} | {row[2]}")


def search_contact():
    """Search for a contact by name and display details if found."""
    name = input("Enter name to search: ")
    found = False

    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Case-insensitive name comparison
            if name.lower() == row["Name"].lower():
                print(f"🙎 Name: {row['Name']} | 📱 Mobile No.: {row['Mobile No.']}")
                found = True

        # Inform user if no matching contact was found
        if not found:
            print("No contact found with this name.")


def main():
    """Main loop to present menu and handle user choices."""
    while True:
        print("\n🫙 Contact Book:\n")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Exit")
        print("---------------------------------------------------")

        choice = input("Enter your choice: ")
        match choice:
            case "1":
                add_contact()
            case "2":
                view_contacts()
            case "3":
                search_contact()
            case "4":
                print("Exiting Contact Book. Goodbye! 👋")
                break
            case _:
                print("Invalid choice. Please try again.")


# Run the main function only when this script is executed directly
if __name__ == "__main__":
    main()
