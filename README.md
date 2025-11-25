# 🫙 Contact Vault

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![CSV](https://img.shields.io/badge/Data-CSV-green.svg)
![CLI](https://img.shields.io/badge/Type-CLI%20Application-orange.svg)
![Storage](https://img.shields.io/badge/Storage-Local%20File-yellow.svg)

## 📋 Overview

**Contact Vault** is a sleek, command-line contact management system built with Python. This application provides a simple yet powerful interface for storing, viewing, and searching contact information with persistent CSV-based storage.

## 🎯 Features

| Feature | Description | Status |
|---------|-------------|--------|
| 📇 **Add Contacts** | Store name, mobile, and email with duplicate prevention | ✅ |
| 📖 **View Contacts** | Display all contacts in a readable format | ✅ |
| 🔍 **Search Contacts** | Find contacts by name (case-insensitive) | ✅ |
| 💾 **Persistent Storage** | CSV-based data persistence | ✅ |
| 🛡️ **Data Validation** | Duplicate name prevention | ✅ |
| 🎨 **User-Friendly UI** | Clear menu with emoji indicators | ✅ |

## 🏗️ Architecture

### 📁 Project Structure
```
DataPlex/
├── 📄 00_contact_vault.py    # Main application file
├── 📄 contacts.csv          # Data storage (auto-created)
└── 📄 README.md             # Documentation
```

### 🔧 Core Components

#### 1. **Data Layer** (`contacts.csv`)
- **Format**: CSV with UTF-8 encoding
- **Columns**: Name, Mobile No., Email ID
- **Location**: Auto-created in project root

#### 2. **Application Layer** (`00_contact_vault.py`)

| Function | Purpose | Key Features |
|----------|---------|--------------|
| `add_contact()` | Add new contacts | Duplicate detection, case-insensitive |
| `view_contacts()` | Display all contacts | Formatted output, empty state handling |
| `search_contact()` | Search by name | Case-insensitive matching |
| `main()` | CLI interface | Menu-driven navigation |

## 🚀 Application Flow

### 📊 User Journey Diagram
```
┌─────────────────┐
│   Start App     │
└─────────┬───────┘
          │
          ▼
┌─────────────────┐
│  Main Menu      │
│  🫙 Contact Book │
└─────────┬───────┘
          │
    ┌─────┴─────┬─────────┬─────────┐
    ▼         ▼         ▼         ▼
┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐
│Add (1)│ │View(2)│ │Search│ │Exit (4)│
└───┬───┘ └───┬───┘ └───┬───┘ └───┬───┘
    │         │         │         │
    ▼         ▼         ▼         ▼
┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
│Get Input│ │Read CSV │ │Get Name │ │Goodbye! │
│Validate │ │Display  │ │Search   │ │         │
│Save Data│ │         │ │Show Results│     │
└─────────┘ └─────────┘ └─────────┘ └─────────┘
```

### 🔄 Data Flow

#### Adding a Contact
1. User selects **"Add New Contact"** (Option 1)
2. System prompts for: Name, Mobile No., Email ID
3. **Validation**: Checks for duplicate names (case-insensitive)
4. **Storage**: Appends to CSV file if unique
5. **Feedback**: Success/error message displayed

#### Viewing Contacts
1. User selects **"View All Contacts"** (Option 2)
2. System reads entire CSV file
3. **Formatting**: Displays as `Name | Mobile No. | Email ID`
4. **Empty State**: Shows "No contacts found" if empty

#### Searching Contacts
1. User selects **"Search Contact"** (Option 3)
2. System prompts for name to search
3. **Matching**: Case-insensitive name comparison
4. **Results**: Shows matching contact or "No contact found"

## 💻 Code Highlights

### 🛡️ Duplicate Prevention
```python
def add_contact():
    name = input("Name: ")
    # Case-insensitive comparison to avoid duplicate names
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if name.lower() == row["Name"].lower():
                print("Contact already exists.")
                return
```

### 📋 Contact Display Format
```python
def view_contacts():
    # Pretty formatting with separators
    for row in rows:
        print(f"{row[0]} | {row[1]} | {row[2]}")
```

### 🔍 Smart Search with Emoji
```python
def search_contact():
    # Enhanced output with visual indicators
    print(f"🙎 Name: {row['Name']} | 📱 Mobile No.: {row['Mobile No.']}")
```

### 🎮 Interactive Menu System
```python
def main():
    while True:
        print("\n🫙 Contact Book:\n")
        print("1. Add New Contact")
        print("2. View All Contacts") 
        print("3. Search Contact")
        print("4. Exit")
        print("---------------------------------------------------")
        
        choice = input("Enter your choice: ")
        match choice:
            case "1": add_contact()
            case "2": view_contacts()
            case "3": search_contact()
            case "4": break
```

## 📊 Data Management

### CSV Structure
```csv
Name,Mobile No.,Email ID
John Doe,1234567890,john@example.com
Jane Smith,0987654321,jane@example.com
```

### File Handling Strategy
- **Auto-creation**: Creates `contacts.csv` on first run
- **UTF-8 Encoding**: Supports international characters
- **Append Mode**: Preserves existing data when adding
- **Error Handling**: Graceful file operations

## 🎨 User Experience Features

### Visual Enhancements
- 📱 **Emojis**: Visual indicators (`🫙`, `🙎`, `📱`)
- 📋 **Clear Formatting**: Consistent separators and spacing
- 🎯 **Intuitive Menu**: Numbered options with clear labels
- ⚡ **Quick Feedback**: Immediate response to user actions

### Input Validation
- ✅ **Duplicate Detection**: Prevents identical names
- 🔤 **Case-Insensitive**: "John" and "john" treated as same
- 📧 **Flexible Email**: Accepts any email format
- 📱 **Phone Format**: Accepts any mobile number format

## 🚀 Getting Started

1. **Run the Application**:
   ```bash
   python 00_contact_vault.py
   ```

2. **Navigate the Menu**: Use number keys (1-4) to select options

3. **Add Your First Contact**: Select option 1 and follow prompts

4. **Explore Features**: Try viewing, searching, and adding more contacts

## 🔧 Technical Specifications

| Aspect | Details |
|--------|---------|
| **Language** | Python 3.x |
| **Storage** | CSV File |
| **Encoding** | UTF-8 |
| **Interface** | Command Line |
| **Dependencies** | Standard Library Only |
| **Platform** | Cross-platform |

## 📈 Future Enhancements

Potential improvements for the Contact Vault:

- 🎨 **Color-coded output** with terminal colors
- 📤 **Export functionality** (JSON, XML formats)
- 🔢 **Contact editing and deletion**
- 📊 **Statistics dashboard** (total contacts, most used domains)
- 🔐 **Password protection** for sensitive contacts
- ☁️ **Cloud sync** capabilities
- 📱 **Mobile app version**

---

*Built with ❤️ using Python's standard library - No external dependencies required!*