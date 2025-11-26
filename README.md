# 🚀 DataPlex Python Suite

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![CLI](https://img.shields.io/badge/Type-CLI%20Applications-orange.svg)
![Storage](https://img.shields.io/badge/Storage-CSV%20%26%20JSON-yellow.svg)
![Database](https://img.shields.io/badge/Database-Local%20File%20Storage-green.svg)
![Education](https://img.shields.io/badge/Purpose-Educational-red.svg)
![Visualization](https://img.shields.io/badge/Features-Data%20Visualization-purple.svg)

## 📋 Overview

**DataPlex** is a collection of sleek, command-line applications built with Python for managing contacts, student grades, movies, weather data, and data visualization. Each application provides a simple yet powerful interface with persistent storage and intuitive user experiences.

## 🎯 Applications Overview

| Application | Purpose | Key Features | Status |
|-----------|---------|--------------|--------|
| 🫙 **Contact Vault** | Contact Management | Add, View, Search contacts | ✅ Complete |
| 📊 **Grade Insight** | Student Grade Analysis | Collect grades, Generate reports | ✅ Complete |
| 🎬 **Cine Archive** | Movie Collection Manager | Add, View, Search movies | ✅ Complete |
| 🌤️ **Weather Logger** | Weather Data Tracker | Log weather, API integration | ✅ Complete |
| 📈 **Graph Craft** | Data Visualization | Weather charts & graphs | ✅ Complete |
| 🔄 **JSON 2 CSV** | Data Format Converter | Convert JSON to CSV | ✅ Complete |

## 🏗️ Project Architecture

### 📁 File Structure
```
DataPlex/
├── 🫙 00_contact_vault.py    # Contact management system
├── 📊 01_grade_insight.py    # Student grade analyzer
├── 🎬 02_cine_archieve.py    # Movie collection manager
├── 🌤️ 03_temp_trail.py      # Weather logging system
├── 📈 04_graph_craft.py      # Data visualization tool
├── � 05_json_2_csv.py       # JSON to CSV converter
├── �📄 contacts.csv           # Contact storage (auto-generated)
├── 📄 movies.json            # Movie database (auto-generated)
├── 📄 weather.csv            # Weather logs (auto-generated)
├── 📄 api_data.json          # Sample API data for converter
├── 📄 converted_data.csv     # Converted data output
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

## 🌤️ Weather Logger - Weather Data Tracker

### 🎯 Core Features
- 🌡️ **Temperature Logging** - Record weather data with API integration
- 🌍 **Multi-City Support** - Track weather for different cities
- 📅 **Date-Based Logging** - Prevent duplicate entries per city per day
- 🌈 **Weather Conditions** - Store weather conditions along with temperature
- 💾 **CSV Storage** - Persistent weather data storage

### 🔧 Technical Implementation

#### **Data Layer** (`weather.csv`)
- **Format**: CSV with UTF-8 encoding
- **Columns**: Date, City, Temperature, Condition
- **Sample Data**:
```csv
Date,City,Temperature,Condition
2025-11-26,Surat,30.12,Clear
2025-11-26,New York,13.96,Mist
```

#### **Core Functions**

| Function | Purpose | Key Features |
|----------|---------|--------------|
| `log_weather()` | Fetch and log weather data | API integration, duplicate prevention |
| `view_logs()` | Display weather history | CSV reading, formatted output |
| `main()` | CLI interface | Menu-driven navigation |

#### 🌡️ Weather API Integration
```python
def log_weather():
    # Get today's date in YYYY-MM-DD format
    date = datetime.now().strftime("%Y-%m-%d")
    city = input("Enter your city name: ").strip()
    
    # Build the API URL with the city name, API key, and metric units
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        
        # Extract temperature and weather condition from the JSON response
        temp = data["main"]["temp"]
        condition = data["weather"][0]["main"]
        
        # Display the weather info to the user
        print(f"🌤️ Temperature in {city} on {date}: {temp}°C — {condition} 🌈")
```

## 📈 Graph Craft - Data Visualization Tool

### 🎯 Core Features
- 📊 **Temperature Trends** - Line chart of daily temperature changes
- 📋 **Weather Condition Analysis** - Bar chart of condition frequencies
- 📈 **Matplotlib Integration** - Professional chart generation
- 🎨 **Interactive Charts** - Zoom, pan, and save capabilities

### 🔧 Technical Implementation

#### **Data Processing**
- **Input**: `weather.csv` file
- **Output**: Interactive matplotlib charts
- **Libraries**: `matplotlib.pyplot`, `collections.defaultdict`

#### **Core Functions**

| Function | Purpose | Key Features |
|----------|---------|--------------|
| `visualize_weather()` | Generate weather charts | Temperature trends, condition frequency |

#### 📊 Chart Generation
```python
def visualize_weather():
    # Lists to store dates and temperatures for the line chart
    dates = []
    temps = []
    # Dictionary to count how many times each weather condition occurs
    conditions = defaultdict(int)

    # Create and display a line chart of daily temperatures
    plt.figure(figsize=(10, 7))
    plt.plot(dates, temps, marker="o")
    plt.title("Daily Temperature Trends")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.tight_layout()
    plt.grid(True)
    plt.show()
```

## 🔄 JSON 2 CSV - Data Format Converter

### 🎯 Core Features
- 🔄 **Format Conversion** - Transform JSON data to CSV format
- 📊 **Data Processing** - Handle complex JSON structures
- 💾 **File Management** - Automatic file creation and validation
- 🛡️ **Error Handling** - Graceful handling of missing or invalid data

### 🔧 Technical Implementation

#### **Data Processing**
- **Input**: `api_data.json` file
- **Output**: `converted_data.csv` file
- **Libraries**: `json`, `csv`, `os`

#### **Core Functions**

| Function | Purpose | Key Features |
|----------|---------|--------------|
| `load_json_data()` | Load JSON from file | Error handling, validation |
| `save_csv_data()` | Save data to CSV | Dictionary to CSV conversion |

#### 🔄 Conversion Process
```python
def load_json_data(filename):
    # Check if the JSON file exists on disk
    if not os.path.exists(filename):
        print("No Json file found.")
        return []
    
    # Open and attempt to parse the JSON file
    with open(filename, "r", encoding="utf-8") as f:
        try:
            return json.load(f)  # Convert JSON text into Python objects
        except:
            print("Invalid JSON format.")
            return []
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
│  📊 Statistics + Analysis   │
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
- **External dependencies**: `requests`, `matplotlib` (for Weather Logger and Graph Craft)

### Installation
```bash
# Install required packages
pip install requests matplotlib
```

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

#### Weather Logger
```bash
python 03_temp_trail.py
```

#### Graph Craft
```bash
python 04_graph_craft.py
```

#### JSON 2 CSV Converter
```bash
python 05_json_2_csv.py
```

## 📈 Technical Specifications

| Aspect | Contact Vault | Grade Insight | Cine Archive | Weather Logger | Graph Craft | JSON 2 CSV |
|--------|---------------|---------------|--------------|----------------|-------------|------------|
| **Language** | Python 3.x | Python 3.x | Python 3.x | Python 3.x | Python 3.x | Python 3.x |
| **Storage** | CSV File | In-memory Dictionary | JSON File | CSV File | CSV File | JSON/CSV |
| **Encoding** | UTF-8 | UTF-8 | UTF-8 | UTF-8 | UTF-8 | UTF-8 |
| **Interface** | Command Line | Command Line | Command Line | Command Line | Chart Display | Command Line |
| **Dependencies** | Standard Library Only | Standard Library Only | Standard Library Only | `requests` | `matplotlib` | Standard Library |
| **Platform** | Cross-platform | Cross-platform | Cross-platform | Cross-platform | Cross-platform | Cross-platform |

## 🎨 User Experience Features

### Visual Enhancements
- 📱 **Emojis**: Visual indicators (`🫙`, `📊`, `🎬`, `🙎`, `📱`, `🍿`, `🎭`, `⭐`, `🌤️`, `📈`)
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

### Weather Logger CSV Structure
```csv
Date,City,Temperature,Condition
2025-11-20,Perth,24.38,Clear
2025-11-21,Perth,19.72,Rain
```

### JSON 2 CSV Sample Data
```json
[
    {
        "id": 101,
        "name": "Alicia Romero",
        "email": "alicia.romero@example.com",
        "age": 29,
        "is_active": true,
        "signup_date": "2024-12-04"
    }
]
```

## 🌟 Key Strengths

1. **🛡️ Robust Error Handling** - All applications handle edge cases gracefully
2. **📱 User-Friendly Interface** - Clear prompts and intuitive navigation
3. **💾 Data Persistence** - Contact Vault, Cine Archive, and Weather Logger maintain data between sessions
4. **📊 Comprehensive Analysis** - Grade Insight provides detailed statistics
5. **🚀 Minimal Dependencies** - Pure Python standard library implementation (except Weather Logger and Graph Craft)
6. **🎨 Professional Presentation** - Clean formatting and visual enhancements
7. **🔍 Smart Search** - Cine Archive offers partial matching capabilities
8. **⭐ Input Validation** - Rating validation in Cine Archive (0-10 range)
9. **📈 Data Visualization** - Graph Craft provides interactive charts
10. **🌐 API Integration** - Weather Logger connects to OpenWeatherMap
11. **🔄 Data Conversion** - JSON 2 CSV enables format flexibility

## 📚 Educational Value

### Learning Outcomes
- 📚 **File I/O Operations** - CSV and JSON file handling
- 📖 **Data Structures** - Dictionaries, lists, and arrays
- 🛡️ **Error Handling** - Try-catch blocks and validation
- 🎮 **CLI Development** - Menu-driven interfaces
- 💾 **Data Persistence** - File-based storage systems
- 🔍 **Search Algorithms** - Case-insensitive partial matching
- 📊 **Data Visualization** - Matplotlib chart generation
- 🔄 **Data Transformation** - JSON to CSV conversion
- � **API Integration** - HTTP requests and JSON parsing

---

*Built with ❤️ using Python. Perfect for learning file handling, data structures, and CLI application development.*