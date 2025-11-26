# 🚀 **DataPlex Python Suite**

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![CLI](https://img.shields.io/badge/Type-CLI%20Applications-orange.svg)
![Storage](https://img.shields.io/badge/Storage-CSV%20%26%20JSON-yellow.svg)
![Database](https://img.shields.io/badge/Database-Local%20File%20Storage-green.svg)
![Education](https://img.shields.io/badge/Purpose-Educational-red.svg)
![Visualization](https://img.shields.io/badge/Features-Data%20Visualization-purple.svg)
![Security](https://img.shields.io/badge/Security-Encryption%20%26%20Base64-blue.svg)

## 📋 **Overview**

**DataPlex** is a comprehensive collection of sleek, command-line applications built with Python for managing contacts, student grades, movies, weather data, data visualization, format conversion, and secure credential storage. Each application provides a simple yet powerful interface with persistent storage and intuitive user experiences.

## 🎯 **Applications Overview**

| Application | Purpose | Key Features | Status |
|-----------|---------|--------------|--------|
| 🫙 **Contact Vault** | Contact Management | Add, View, Search contacts | ✅ Complete |
| 📊 **Grade Insight** | Student Grade Analysis | Collect grades, Generate reports | ✅ Complete |
| 🎬 **Cine Archive** | Movie Collection Manager | Add, View, Search movies | ✅ Complete |
| 🌤️ **Weather Logger** | Weather Data Tracker | Log weather, API integration | ✅ Complete |
| 📈 **Graph Craft** | Data Visualization | Weather charts & graphs | ✅ Complete |
| 🔄 **JSON 2 CSV** | Data Format Converter | Convert JSON to CSV | ✅ Complete |
| 🔄 **CSV 2 JSON** | Data Format Converter | Convert CSV to JSON | ✅ Complete |
| 🔧 **JSON Simplify** | JSON Flattener | Flatten nested JSON structures | ✅ Complete |
| 🔐 **Pass Fort** | Password Manager | Store credentials securely | ✅ Complete |
| 📝 **Sym Shield** | Secure Notes Manager | Encrypt/decrypt notes | ✅ Complete |

## 🏗️ **Project Architecture**

### 📁 **File Structure**
```
DataPlex/
├── 🫙 00_contact_vault.py    # Contact management system
├── 📊 01_grade_insight.py    # Student grade analyzer
├── 🎬 02_cine_archieve.py    # Movie collection manager
├── 🌤️ 03_temp_trail.py      # Weather logging system
├── 📈 04_graph_craft.py      # Data visualization tool
├── 🔄 05_json_2_csv.py       # JSON to CSV converter
├── 🔄 06_csv_2_json.py       # CSV to JSON converter
├── 🔧 07_json_simplify.py    # JSON flattening utility
├── 🔐 08_pass_fort.py        # Password manager
├── 📝 09_sym_shield.py       # Secure notes manager
├── 📄 contacts.csv           # Contact storage (auto-generated)
├── 📄 movies.json            # Movie database (auto-generated)
├── 📄 weather.csv            # Weather logs (auto-generated)
├── 📄 api_data.json          # Sample API data for converter
├── 📄 nested_data.json       # Sample nested JSON data
├── 📄 notes.json             # Encrypted notes storage
├── 🔑 vault.key              # Encryption key for notes
├── 📄 vault.txt              # Base64 encoded credentials
└── 📖 README.md              # Project documentation
```

## 🫙 **Contact Vault - Contact Management System**

### 🎯 **Core Features**
- ✅ **Add Contacts** - Store name, mobile, and email with duplicate prevention
- 📖 **View Contacts** - Display all contacts in a readable format
- 🔍 **Search Contacts** - Find contacts by name (case-insensitive)
- 💾 **Persistent Storage** - CSV-based data persistence
- 🛡️ **Data Validation** - Duplicate name prevention
- 🎨 **User-Friendly UI** - Clear menu with emoji indicators

### 🔧 **Technical Implementation**

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

### 💡 **Code Highlights**

#### 🛡️ **Duplicate Prevention System**
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

#### 🎨 **Enhanced Search Display**
```python
def search_contact():
    # Enhanced output with visual indicators
    print(f"🙎 Name: {row['Name']} | 📱 Mobile No.: {row['Mobile No.']}")
```

#### 🎮 **Interactive Menu System**
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

## 📊 **Grade Insight - Student Grade Analyzer**

### 🎯 **Core Features**
- 📥 **Data Collection** - Interactive student grade input
- 📈 **Statistical Analysis** - Calculate averages, highest/lowest marks
- 🏆 **Performance Recognition** - Identify top performers and struggling students
- 📋 **Detailed Reports** - Comprehensive grade summaries
- 🛡️ **Input Validation** - Handle invalid inputs gracefully

### 🔧 **Technical Implementation**

#### **Data Storage**
- **Format**: In-memory dictionary during runtime
- **Structure**: `students = {"name": marks, ...}`
- **Persistence**: Session-based (no file storage)

#### **Core Functions**

| Function | Purpose | Key Features |
|----------|---------|--------------|
| `collect_students_data()` | Interactive data collection | Duplicate prevention, input validation, 'done' termination |
| `display_students_report()` | Comprehensive report generation | Statistics calculation, formatted output, performance analysis |

### 📊 **Code Highlights**

#### 🛡️ **Input Validation & Duplicate Prevention**
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

#### 📈 **Statistical Analysis & Report Generation**
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

#### 📋 **Professional Report Formatting**
```python
print("-" * 50)
print(" Student Report Card 📇 ")
print(f"Total Number of Students: {len(students)}")
print(f"Average Marks of Students: {average_marks:.2f}")
print(f"Highest Marks: {highest_marks:.2f} by {', '.join(topper)}")
print(f"Lowest Marks: {lowest_marks:.2f} by {', '.join(lower)}")
print("-" * 50)
```

## 🎬 **Cine Archive - Movie Collection Manager**

### 🎯 **Core Features**
- 🎞️ **Add Movies** - Store title, genre, and rating with duplicate prevention
- 📺 **View Collection** - Display all movies in formatted list
- 🔍 **Smart Search** - Search by title or genre (partial, case-insensitive)
- 💾 **JSON Storage** - Persistent movie database
- ⭐ **Rating Validation** - Ensure ratings are between 0-10
- 🎭 **Rich Display** - Emoji-enhanced movie listings

### 🔧 **Technical Implementation**

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

### 🎬 **Code Highlights**

#### 🛡️ **Duplicate Prevention & Rating Validation**
```python
def add_movie(movies):
    title = input("Enter Movie Title: ").strip()
    
    # Prevent duplicate titles (case-insensitive check)
    if any(movie["title"].lower() == title.lower() for movie in movies):
        print("Movie with this title already exists.")
        return
    
    genre = input("Enter Movie Genre: ").strip()
    
    # Validate rating: must be a number between 0 and 10
    try:
        rating = float(input("Enter Movie Rating (0-10): ").strip())
        if not (0 <= rating <= 10):
            raise ValueError
    except ValueError:
        print("Invalid Rating. Please enter a number between 0-10.")
        return
```

#### 🎭 **Rich Display Formatting**
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

#### 🔍 **Smart Search Implementation**
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

## 🌤️ **Weather Logger - Weather Data Tracker**

### 🎯 **Core Features**
- 🌡️ **Temperature Logging** - Record weather data with API integration
- 🌍 **Multi-City Support** - Track weather for different cities
- 📅 **Date-Based Logging** - Prevent duplicate entries per city per day
- 🌈 **Weather Conditions** - Store weather conditions along with temperature
- 💾 **CSV Storage** - Persistent weather data storage

### 🔧 **Technical Implementation**

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

#### 🌡️ **Weather API Integration**
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

## 📈 **Graph Craft - Data Visualization Tool**

### 🎯 **Core Features**
- 📊 **Temperature Trends** - Line chart of daily temperature changes
- 📋 **Weather Condition Analysis** - Bar chart of condition frequencies
- 📈 **Matplotlib Integration** - Professional chart generation
- 🎨 **Interactive Charts** - Zoom, pan, and save capabilities

### 🔧 **Technical Implementation**

#### **Data Processing**
- **Input**: `weather.csv` file
- **Output**: Interactive matplotlib charts
- **Libraries**: `matplotlib.pyplot`, `collections.defaultdict`

#### **Core Functions**

| Function | Purpose | Key Features |
|----------|---------|--------------|
| `visualize_weather()` | Generate weather charts | Temperature trends, condition frequency |

#### 📊 **Chart Generation**
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

## 🔄 **JSON 2 CSV - Data Format Converter**

### 🎯 **Core Features**
- 🔄 **Format Conversion** - Transform JSON data to CSV format
- 📊 **Data Processing** - Handle complex JSON structures
- 💾 **File Management** - Automatic file creation and validation
- 🛡️ **Error Handling** - Graceful handling of missing or invalid data

### 🔧 **Technical Implementation**

#### **Data Processing**
- **Input**: `api_data.json` file
- **Output**: `converted_data.csv` file
- **Libraries**: `json`, `csv`, `os`

#### **Core Functions**

| Function | Purpose | Key Features |
|----------|---------|--------------|
| `load_json_data()` | Load JSON from file | Error handling, validation |
| `save_csv_data()` | Save data to CSV | Dictionary to CSV conversion |

#### 🔄 **Conversion Process**
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

## 🔄 **CSV 2 JSON - Data Format Converter**

### 🎯 **Core Features**
- 🔄 **Reverse Conversion** - Transform CSV data to JSON format
- 📋 **Data Preview** - Show sample of converted data
- 💾 **Bidirectional Flow** - Works with existing conversion pipeline
- 🛡️ **Validation** - Check file existence and data integrity

### 🔧 **Technical Implementation**

#### **Data Processing**
- **Input**: `converted_data.csv` file
- **Output**: `converted_data.json` file
- **Libraries**: `json`, `csv`, `os`

#### **Core Functions**

| Function | Purpose | Key Features |
|----------|---------|--------------|
| `load_csv_data()` | Load CSV from file | DictReader implementation |
| `save_json_data()` | Save data to JSON | Pretty formatting with indent |
| `preview_json_data()` | Display sample data | Configurable preview count |

## 🔧 **JSON Simplify - JSON Flattener**

### 🎯 **Core Features**
- 🔧 **Nested JSON Flattening** - Convert complex nested structures to flat key-value pairs
- 🎯 **Recursive Processing** - Handle deeply nested objects and arrays
- 💾 **Data Transformation** - Simplify JSON for easier analysis
- 🛡️ **Type Safety** - Handle different data types appropriately

### 🔧 **Technical Implementation**

#### **Data Processing**
- **Input**: `nested_data.json` file
- **Output**: `simplified_data.json` file
- **Libraries**: `json`, `os`

#### **Core Functions**

| Function | Purpose | Key Features |
|----------|---------|--------------|
| `flatten_json()` | Recursive flattening | Handle nested objects and arrays |
| `main()` | Process workflow | Load, flatten, save data |

#### 🔧 **Recursive Flattening Algorithm**
```python
def flatten_json(data, parent_key="", sep="_"):
    """
    Recursively flattens a nested JSON structure into a single-level dictionary.
    
    Args:
        data: The JSON data (dict, list, or primitive value).
        parent_key: The accumulated key string from parent levels.
        sep: The separator used to join nested keys.
    
    Returns:
        A dictionary with flattened keys and corresponding values.
    """
    items = {}

    # If data is a dictionary, iterate through its key-value pairs
    if isinstance(data, dict):
        for k, v in data.items():
            # Build the full key by appending the current key to the parent key
            full_key = f"{parent_key}{sep}{k}" if parent_key else k
            print(full_key)  # Debug: print the current key being processed
            # Recursively flatten the value and update items
            items.update(flatten_json(v, full_key, sep=sep))
```

## 🔐 **Pass Fort - Password Manager**

### 🎯 **Core Features**
- 🔐 **Credential Storage** - Store website credentials securely
- 🔒 **Base64 Encoding** - Light obfuscation for password protection
- 📊 **Password Strength** - Analyze and display password strength
- 💾 **Vault Storage** - Persistent credential storage in text file

### 🔧 **Technical Implementation**

#### **Data Storage**
- **Format**: Text file with base64 encoded credentials
- **File**: `vault.txt` (auto-generated)
- **Security**: Base64 encoding (light obfuscation)

#### **Core Functions**

| Function | Purpose | Key Features |
|----------|---------|--------------|
| `add_credential()` | Store new credentials | Password strength analysis |
| `view_credentials()` | Display stored credentials | Base64 decoding |
| `password_strength()` | Analyze password strength | Multi-factor validation |

#### 🔒 **Security Implementation**
```python
def encode(text):
    """
    Encode plain text to base64 string.
    This provides a very light obfuscation (NOT secure encryption).
    """
    return base64.b64encode(text.encode()).decode()

def password_strength(password):
    """
    Return a qualitative strength label for the given password.
    Checks length, upper/lower cases, digits, and special characters.
    """
    strength = 0
    if len(password) >= 8:
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in "!@#$%^&*()" for c in password):
        strength += 1
```

## 📝 **Sym Shield - Secure Notes Manager**

### 🎯 **Core Features**
- 🔐 **Note Encryption** - Store notes with Fernet symmetric encryption
- 📝 **Note Management** - Add, view, and manage encrypted notes
- 🔑 **Key Management** - Automatic key generation and storage
- 💾 **Persistent Storage** - JSON-based encrypted note storage
- 📅 **Timestamp Tracking** - Record creation dates for notes

### � **Technical Implementation**

#### **Data Storage**
- **Format**: JSON file with Fernet encrypted content
- **Files**: `notes.json` (encrypted notes), `vault.key` (encryption key)
- **Security**: Fernet symmetric encryption (cryptographically secure)

#### **Core Functions**

| Function | Purpose | Key Features |
|----------|---------|--------------|
| `load_or_generate_key()` | Key management | Fernet key generation and storage |
| `add_note()` | Create encrypted notes | Fernet encryption with timestamps |
| `view_notes()` | Display decrypted notes | Fernet decryption, formatted output |
| `delete_note()` | Remove notes | Index-based deletion with validation |

#### 🔐 **Encryption Implementation**
```python
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
```

## �📊 **Application Flow Diagrams**

### 🫙 **Contact Vault Flow**
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

### 📊 **Grade Insight Flow**
```
┌─────────────────┐
│   Start App     │
└─────────┬───────┘
          │
          ▼
┌─────────────────┐
│  Data Collection│
│  📥 Enter Grades │
└─────────┬───────┘
          │
          ▼
┌─────────────────┐
│  Process Data   │
│  📈 Calculate   │
│  Statistics     │
└─────────┬───────┘
          │
          ▼
┌─────────────────┐
│  Generate Report│
│  📋 Display     │
│  Summary        │
└─────────────────┘
```

### 🔐 **Security Architecture**

| Application | Security Level | Method | Purpose |
|-------------|----------------|---------|---------|
| **Pass Fort** | Light Obfuscation | Base64 Encoding | Credential storage |
| **Sym Shield** | Strong Encryption | Fernet (AES 128) | Note encryption |
| **All Apps** | Data Validation | Input Sanitization | Prevent errors |

## �️ **Technical Dependencies**

### 📦 **Core Libraries**
```
certifi==2025.11.12          # SSL certificate verification
chardet==3.0.4               # Character encoding detection
idna==2.10                   # Internationalized domain names
requests==2.25.1             # HTTP library for API calls
matplotlib==3.3.4            # Data visualization
numpy==1.19.5                # Numerical computing
cryptography==3.4.8          # Encryption algorithms
```

### 🔧 **Built-in Modules**
- `csv` - CSV file handling
- `json` - JSON processing
- `os` - Operating system interface
- `datetime` - Date and time operations
- `base64` - Base64 encoding/decoding
- `collections` - Specialized container datatypes

## 🚀 **Getting Started**

### ⚡ **Quick Start**
1. **Choose your application**: Each `.py` file is a standalone CLI tool
2. **Run the script**: `python 00_contact_vault.py` (or any other app)
3. **Follow the prompts**: Each app has intuitive menu-driven navigation
4. **Data persists automatically**: All data is saved to local files

### 🔑 **API Configuration**
- **Weather Logger**: Replace `"Enter your OpenWeatherMap API key here"` with your actual API key
- **All other apps**: Work out-of-the-box with local file storage

## 💡 **Usage Examples**

### 🫙 **Contact Vault**
```bash
$ python 00_contact_vault.py
🫙 Contact Book:
1. Add New Contact
2. View All Contacts
3. Search Contact
4. Exit
---------------------------------------------------
Enter your choice: 1
Name: John Doe
Mobile No.: +1234567890
Email ID: john@example.com
Contact added successfully.
```

### � **Grade Insight**
```bash
$ python 01_grade_insight.py
Enter student name (or 'done' to finish): Alice
Enter the marks for Alice: 95
Enter student name (or 'done' to finish): Bob
Enter the marks for Bob: 87
Enter student name (or 'done' to finish): done
--------------------------------------------------
 Student Report Card 📇 
Total Number of Students: 2
Average Marks of Students: 91.00
Highest Marks: 95.00 by Alice
Lowest Marks: 87.00 by Bob
--------------------------------------------------
```

### 🌤️ **Weather Logger**
```bash
$ python 03_temp_trail.py
🌤️ Weather Logger
1. Log Weather
2. View Logs
3. Exit
Enter your choice: 1
Enter your city name: London
🌤️ Temperature in London on 2025-11-26: 12.5°C — Clouds 🌈
Weather data logged successfully.
```

## 🎨 **Visual Features**

### 📊 **Chart Generation**
- **Line Charts**: Temperature trends over time
- **Bar Charts**: Weather condition frequency analysis
- **Interactive Elements**: Zoom, pan, save charts
- **Professional Styling**: Grid lines, markers, proper labels

### 🎭 **Emoji Integration**
- 🫙 Contact book with contact emojis
- 📊 Grade reports with academic emojis
- 🎬 Movie database with entertainment emojis
- �️ Weather data with weather condition emojis
- 🔐 Security features with lock/shield emojis

## 🔒 **Security Features**

### 🛡️ **Data Protection**
- **Input Validation**: All user inputs are validated
- **Duplicate Prevention**: Built-in checks for existing data
- **Error Handling**: Graceful handling of invalid inputs
- **File Safety**: Automatic file creation and UTF-8 encoding

### 🔐 **Encryption Methods**
- **Base64 Encoding**: Light obfuscation for passwords (Pass Fort)
- **Fernet Encryption**: Strong AES-128 encryption for notes (Sym Shield)
- **Key Management**: Automatic key generation and secure storage

## 📈 **Data Management**

### 💾 **Storage Formats**
- **CSV Files**: Contact vault, weather data (easy to read/edit)
- **JSON Files**: Movie database, converted data (structured storage)
- **Text Files**: Encrypted credentials (base64 encoded)
- **Encrypted JSON**: Secure notes (Fernet encrypted)

### 🔄 **Data Conversion Pipeline**
```
JSON Data → CSV Converter → CSV Data → JSON Converter → JSON Data
     ↓                                                      ↓
Nested JSON → Flattener → Flat JSON → Analysis → Insights
```

## 🎯 **Educational Value**

### 📚 **Learning Outcomes**
- **File I/O Operations**: Reading/writing different file formats
- **Data Structures**: Dictionaries, lists, JSON objects
- **API Integration**: HTTP requests and JSON parsing
- **Data Visualization**: Matplotlib chart generation
- **Security Concepts**: Encryption and data protection
- **Error Handling**: Try-catch blocks and validation
- **CLI Design**: Menu-driven user interfaces

### 🔧 **Programming Concepts**
- **Functions**: Modular code organization
- **File Handling**: CSV, JSON, and text file operations
- **Data Processing**: Parsing, validation, transformation
- **User Experience**: Emoji integration and formatting
- **Security**: Encryption and encoding techniques
- **Visualization**: Chart generation and data representation

---

## 🌟 **Project Highlights**

✅ **Complete CLI Suite** - 10 fully functional applications  
✅ **Professional Code Quality** - Clean, documented, and organized  
✅ **Educational Focus** - Perfect for learning Python concepts  
✅ **Real-World Applications** - Practical tools for daily use  
✅ **Data Visualization** - Professional charts and graphs  
✅ **Security Features** - Encryption and data protection  
✅ **Emoji Integration** - Modern, user-friendly interface  
✅ **Persistent Storage** - All data saved automatically  
✅ **Error Handling** - Robust input validation  
✅ **Modular Design** - Each app works independently  

---

*🚀 **DataPlex Python Suite** - Your comprehensive toolkit for data management, visualization, and security in the command line!*