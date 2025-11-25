# 🚀 DataPlex Python Suite

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![CLI](https://img.shields.io/badge/Type-CLI%20Applications-orange.svg)
![Storage](https://img.shields.io/badge/Storage-CSV%20%26%20JSON-yellow.svg)
![Database](https://img.shields.io/badge/Database-Local%20File%20Storage-green.svg)
![Education](https://img.shields.io/badge/Purpose-Educational-red.svg)

## 📋 Overview

**DataPlex** is a collection of sleek, command-line applications built with Python for managing contacts, student grades, and movie collections. Each application provides a simple yet powerful interface with persistent storage and intuitive user experiences.

## 🎯 Applications Overview

| Application | Purpose | Key Features | Status |
|-----------|---------|--------------|--------|
| 🫙 **Contact Vault** | Contact Management | Add, View, Search contacts | ✅ Complete |
| 📊 **Grade Insight** | Student Grade Analysis | Collect grades, Generate reports | ✅ Complete |
| 🎬 **Cine Archive** | Movie Collection Manager | Add, View, Search movies | ✅ Complete |

## 🏗️ Project Architecture

### 📁 File Structure
```
DataPlex/
├── 🫙 00_contact_vault.py    # Contact management system
├── 📊 01_grade_insight.py    # Student grade analyzer
├── 🎬 02_cine_archieve.py    # Movie collection manager
├── 📄 contacts.csv           # Contact storage (auto-generated)
├── 📄 movies.json            # Movie database (auto-generated)
└── 📖 README.md              # Project documentation
```

## 🫙 Contact Vault - Contact Management System

### 🎯 Core Features
- ✅ **Add Contacts** - Store name, mobile, and email with duplicate prevention
- 📖 **View Contacts** - Display all contacts in a readable format
- 🔍 **Search Contacts** - Find contacts by name (case-insensitive)
- 💾 **Persistent Storage** - CSV-based data persistence
- 🛡️ **Data Validation** - Duplicate name prevention
- 🎨 **User-Friendly UI** - Clear menu with emoji indicators

### 🔧 Technical Implementation

#### **Data Layer** (`contacts.csv`)
- **Format**: CSV with UTF-8 encoding
- **Columns**: Name, Mobile No., Email ID
- **Location**: Auto-created in project root

#### **Core Functions**

| Function | Purpose | Key Features |
|----------|---------|--------------|
| `add_contact()` | Add new contacts | Duplicate detection, case-insensitive validation |
| `view_contacts()` | Display all contacts | Formatted output, empty state handling |
| `search_contact()` | Search by name | Case-insensitive matching, emoji-enhanced display |
| `main()` | CLI interface | Menu-driven navigation with match-case structure |

### 💡 Code Highlights

#### 🛡️ Duplicate Prevention System
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

#### 🎨 Enhanced Search Display
```python
def search_contact():
    # Enhanced output with visual indicators
    print(f"🙎 Name: {row['Name']} | 📱 Mobile No.: {row['Mobile No.']}")
```

#### 🎮 Interactive Menu System
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

## 📊 Grade Insight - Student Grade Analyzer

### 🎯 Core Features
- 📥 **Data Collection** - Interactive student grade input
- 📈 **Statistical Analysis** - Calculate averages, highest/lowest marks
- 🏆 **Performance Recognition** - Identify top performers and struggling students
- 📋 **Detailed Reports** - Comprehensive grade summaries
- 🛡️ **Input Validation** - Handle invalid inputs gracefully

### 🔧 Technical Implementation

#### **Data Storage**
- **Format**: In-memory dictionary during runtime
- **Structure**: `students = {"name": marks, ...}`
- **Persistence**: Session-based (no file storage)

#### **Core Functions**

| Function | Purpose | Key Features |
|----------|---------|--------------|
| `collect_students_data()` | Interactive data collection | Duplicate prevention, input validation, 'done' termination |
| `display_students_report()` | Comprehensive report generation | Statistics calculation, formatted output, performance analysis |

### 📊 Code Highlights

#### 🛡️ Input Validation & Duplicate Prevention
```python
def collect_students_data():
    while True:
        name = input("Enter student name (or 'done' to finish): ")
        
        if name.lower() == "done":
            break
        # Check if the student has already been entered
        if name in students:
            print("Student already exists.")
            continue
```

#### 📈 Statistical Analysis & Report Generation
```python
def display_students_report(students):
    # Extract all marks into a list for easy calculation
    marks = list(students.values())
    highest_marks = max(marks)
    lowest_marks = min(marks)
    average_marks = sum(marks) / len(marks)
    
    # Find all students who achieved the highest and lowest marks
    topper = [name for name, score in students.items() if score == highest_marks]
    lower = [name for name, score in students.items() if score == lowest_marks]
```

#### 📋 Professional Report Formatting
```python
print("-" * 50)
print(" Student Report Card 📇 ")
print(f"Total Number of Students: {len(students)}")
print(f"Average Marks of Students: {average_marks:.2f}")
print(f"Highest Marks: {highest_marks:.2f} by {', '.join(topper)}")
print(f"Lowest Marks: {lowest_marks:.2f} by {', '.join(lower)}")
print("-" * 50)
```

## 🎬 Cine Archive - Movie Collection Manager

### 🎯 Core Features
- 🎞️ **Add Movies** - Store title, genre, and rating with duplicate prevention
- 📺 **View Collection** - Display all movies in formatted list
- 🔍 **Smart Search** - Search by title or genre (partial, case-insensitive)
- 💾 **JSON Storage** - Persistent movie database
- ⭐ **Rating Validation** - Ensure ratings are between 0-10
- 🎭 **Rich Display** - Emoji-enhanced movie listings

### 🔧 Technical Implementation

#### **Data Layer** (`movies.json`)
- **Format**: JSON with UTF-8 encoding
- **Structure**: Array of movie objects with title, genre, rating
- **Location**: Auto-created in project root
- **Sample Data**:
```json
[
  {
    "title": "Dil Ke Safar",
    "genre": "Romantic Drama",
    "rating": 8.1
  }
]
```

#### **Core Functions**

| Function | Purpose | Key Features |
|----------|---------|--------------|
| `load_movies()` | Load movie database | JSON file reading, error handling |
| `save_movie()` | Persist movie data | JSON file writing with formatting |
| `add_movie()` | Add new movies | Duplicate detection, rating validation |
| `view_movies()` | Display collection | Formatted output with emojis |
| `search_movie()` | Smart search | Partial matching, case-insensitive |
| `run_movie_db()` | Main interface | Menu-driven navigation |

### 🎬 Code Highlights

#### 🛡️ Duplicate Prevention & Rating Validation
```python
def add_movie(movies):
    title = input("Enter Movie Title: ").strip()
    
    # Prevent duplicate titles (case-insensitive check)
    if any(movie["title"].lower() == title.lower() for movie in movies):
        print("Movie with this title already exists.")
        return
    
    # Validate rating: must be a number between 0 and 10
    try:
        rating = float(input("Enter Movie Rating (0-10): ").strip())
        if not (0 <= rating <= 10):
            raise ValueError
    except ValueError:
        print("Invalid Rating. Please enter a number between 0-10.")
        return
```

#### 🎭 Rich Display Formatting
```python
def view_movies(movies):
    if not movies:
        print("No Movies Found.")
        return
    print("-" * 40)
    print("🍿 Movie Database 🍿")
    for movie in movies:
        print(f"🎬 {movie['title']} | 🎭 {movie['genre']} | ⭐ {movie['rating']}")
    print("-" * 40)
```

#### 🔍 Smart Search Implementation
```python
def search_movie(movies):
    search_term = input("Enter Title or Genre to Search: ").strip()
    
    # Collect movies whose title or genre contains the search term
    results = [
        movie
        for movie in movies
        if search_term.lower() in movie["title"].lower()
        or search_term.lower() in movie["genre"].lower()
    ]
```

## 📊 Application Flow Diagrams

### 🫙 Contact Vault Flow
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
│Validate │ │Read CSV │ │Get Name │ │Goodbye! │
│Save Data│ │Display  │ │Search   │ │         │
└─────────┘ └─────────┘ └─────────┘ └─────────┘
```

### 📊 Grade Insight Flow
```
┌─────────────────┐
│   Start App     │
└─────────┬───────┘
          │
          ▼
┌─────────────────────────────┐
│  Collect Student Data       │
│  📥 Interactive Input Loop  │
└─────────┬───────────────────┘
          │
          ▼
┌─────────────────────────────┐
│  Generate Report            │
│  📊 Statistics + Analysis │
└─────────┬───────────────────┘
          │
          ▼
┌─────────────────┐
│   Display Results│
│   📋 Full Report │
└─────────────────┘
```

### 🎬 Cine Archive Flow
```
┌─────────────────┐
│   Start App     │
└─────────┬───────┘
          │
          ▼
┌─────────────────────────────┐
│  Load Movie Database        │
│  📄 Read movies.json        │
└─────────┬───────────────────┘
          │
          ▼
┌─────────────────┐
│  Main Menu      │
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
│Validate │ │Display  │ │Search   │ │Save &   │
│Save JSON│ │Movies   │ │Database │ │Exit     │
└─────────┘ └─────────┘ └─────────┘ └─────────┘
```

## 🚀 Getting Started

### Prerequisites
- **Python 3.x** installed on your system
- **No external dependencies** required (uses standard library only)

### Running the Applications

#### Contact Vault
```bash
python 00_contact_vault.py
```

#### Grade Insight
```bash
python 01_grade_insight.py
```

#### Cine Archive
```bash
python 02_cine_archieve.py
```

## 📈 Technical Specifications

| Aspect | Contact Vault | Grade Insight | Cine Archive |
|--------|---------------|---------------|--------------|
| **Language** | Python 3.x | Python 3.x | Python 3.x |
| **Storage** | CSV File | In-memory Dictionary | JSON File |
| **Encoding** | UTF-8 | UTF-8 | UTF-8 |
| **Interface** | Command Line | Command Line | Command Line |
| **Dependencies** | Standard Library Only | Standard Library Only | Standard Library Only |
| **Platform** | Cross-platform | Cross-platform | Cross-platform |

## 🎨 User Experience Features

### Visual Enhancements
- 📱 **Emojis**: Visual indicators (`🫙`, `📊`, `🎬`, `🙎`, `📱`, `🍿`, `🎭`, `⭐`)
- 📋 **Clear Formatting**: Consistent separators and spacing
- 🎯 **Intuitive Menus**: Numbered options with clear labels
- ⚡ **Quick Feedback**: Immediate response to user actions

### Input Validation
- ✅ **Duplicate Detection**: Prevents identical entries
- 🔤 **Case-Insensitive**: Smart string comparison
- ⚠️ **Error Handling**: Graceful handling of invalid inputs
- 🔄 **Flexible Formats**: Accepts various input formats

## 📊 Data Management

### Contact Vault CSV Structure
```csv
Name,Mobile No.,Email ID
John Doe,1234567890,john@example.com
Jane Smith,0987654321,jane@example.com
```

### Grade Insight Data Flow
```python
# Input Collection
students = {
    "Alice": 85.5,
    "Bob": 92.0,
    "Charlie": 78.5
}

# Report Generation
# Average: 85.33
# Highest: 92.0 (Bob)
# Lowest: 78.5 (Charlie)
```

### Cine Archive JSON Structure
```json
[
  {
    "title": "Dil Ke Safar",
    "genre": "Romantic Drama",
    "rating": 8.1
  },
  {
    "title": "Mumbai Nights",
    "genre": "Action / Crime",
    "rating": 7.4
  }
]
```

## 🌟 Key Strengths

1. **🛡️ Robust Error Handling** - All applications handle edge cases gracefully
2. **📱 User-Friendly Interface** - Clear prompts and intuitive navigation
3. **💾 Data Persistence** - Contact Vault and Cine Archive maintain data between sessions
4. **📊 Comprehensive Analysis** - Grade Insight provides detailed statistics
5. **🚀 Zero Dependencies** - Pure Python standard library implementation
6. **🎨 Professional Presentation** - Clean formatting and visual enhancements
7. **🔍 Smart Search** - Cine Archive offers partial matching capabilities
8. **⭐ Input Validation** - Rating validation in Cine Archive (0-10 range)

## � Educational Value

### Learning Outcomes
- 📚 **File I/O Operations** - CSV and JSON file handling
- � **Data Structures** - Dictionaries, lists, and arrays
- �️ **Error Handling** - Try-catch blocks and validation
- 🎮 **CLI Development** - Menu-driven interfaces
- � **Data Persistence** - File-based storage systems
- � **Search Algorithms** - Case-insensitive partial matching

### Code Quality Features
- � **Clear Documentation** - Comprehensive docstrings
- 🏗️ **Modular Design** - Separate functions for each feature
- � **Consistent Patterns** - Similar structure across applications
- 🎯 **Single Responsibility** - Each function has one clear purpose

---

*Built with ❤️ using Python's standard library - No external dependencies required!*

**🎯 Perfect for educational purposes, personal productivity, and learning Python CLI development!**