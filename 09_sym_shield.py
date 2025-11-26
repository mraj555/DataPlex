import os
import json
from cryptography.fernet import Fernet
from datetime import datetime

# File names for storing encrypted notes and the encryption key
NOTE_VAULT = "notes.json"
KEY_FILE = "vault.key"


def load_or_generate_key():
    """
    Load the encryption key from disk if it exists; otherwise generate a new one and save it.
    Returns a Fernet instance ready for encryption/decryption.
    """
    if not os.path.exists(KEY_FILE):
        # Generate a fresh symmetric key and save it to disk
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
    else:
        # Read the existing key from disk
        with open(KEY_FILE, "rb") as f:
            key = f.read()

    return Fernet(key)

# Global Fernet instance used throughout the script
fernet = load_or_generate_key()


def load_vault():
    """
    Load the JSON file containing all encrypted notes.
    Returns an empty list if the file does not exist.
    """
    if not os.path.exists(NOTE_VAULT):
        print("No vault file found.")
        return []

    with open(NOTE_VAULT, "r", encoding="utf-8") as f:
        return json.load(f)


def save_vault(notes):
    """
    Save the provided list of notes (dicts) to the JSON vault file.
    """
    with open(NOTE_VAULT, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2)


def add_note():
    """
    Prompt the user for a note title and content, encrypt the content,
    append the note to the vault, and save it back to disk.
    """
    title = input("Enter your note title: ").strip()
    content = input("Enter your note content: ").strip()

    # Record the current time as a string
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Load existing notes, encrypt the new content, and append the new note
    data = load_vault()
    encrypted_content = fernet.encrypt(content.encode()).decode()
    data.append(
        {
            "title": title,
            "content": encrypted_content,
            "timestamp": timestamp,
        }
    )

    # Persist the updated vault
    save_vault(data)
    print("✅ Note added successfully.")


def list_notes():
    """
    Display a numbered list of all note titles with their timestamps.
    """
    data = load_vault()
    if not data:
        print("No notes found.")
        return

    for i, note in enumerate(data, 1):
        print(f"{i}. {note['title']} - {note['timestamp']}")


def view_note():
    """
    List all notes, then prompt the user to pick one by number.
    Decrypt and display the selected note's full content.
    """
    list_notes()
    try:
        index = int(input("Enter the note number to view: ").strip()) - 1
        data = load_vault()
        # Validate index range
        if 0 <= index < len(data):
            note = data[index]
            # Decrypt the stored content before displaying
            decrypted_content = fernet.decrypt(note["content"].encode()).decode()
            print(
                f"\n📝 Title: {note['title']} - Timestamp: {note['timestamp']}\nContent: {decrypted_content}"
            )
        else:
            print("Invalid note number.")

    except ValueError:
        print("Invalid input. Please enter a number.")
        return


def search_notes():
    """
    Prompt the user for a search query, then list all notes whose titles
    contain the query (case-insensitive). Decrypt and show the content of each match.
    """
    query = input("Enter search query: ").strip()
    data = load_vault()
    # Filter notes by title containing the query
    results = [note for note in data if query.lower() in note["title"].lower()]

    if not results:
        print("No notes found.")
        return
    else:
        for i, note in enumerate(results, 1):
            decrypted_content = fernet.decrypt(note["content"].encode()).decode()
            print(
                f"{i}. {note['title']} - {note['timestamp']}\nContent: {decrypted_content}"
            )


def main():
    """
    Main interactive loop presenting a menu to the user.
    Handles user choices and delegates to appropriate functions.
    """
    while True:
        print("\n--- Symmetric Shield ---")
        print("1. Add Note")
        print("2. List Notes")
        print("3. View Note")
        print("4. Search Notes")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        match choice:
            case "1":
                add_note()
            case "2":
                list_notes()
            case "3":
                view_note()
            case "4":
                search_notes()
            case "5":
                print("Exiting Symmetric Shield.")
                break
            case _:
                print("Invalid choice. Please try again.")


# Run the main menu loop only when this script is executed directly
if __name__ == "__main__":
    main()
