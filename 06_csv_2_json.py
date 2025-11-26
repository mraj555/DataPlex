import os
import json
import csv

# Define the input CSV file and the output JSON file paths
INPUT_FILE = "converted_data.csv"
OUTPUT_FILE = "converted_data.json"


def load_csv_data(filename):
    """
    Load data from a CSV file and return it as a list of dictionaries.
    Each dictionary represents a row, with column headers as keys.
    """
    # Check if the specified file exists
    if not os.path.exists(filename):
        print(f"Error: {filename} does not exist.")
        return []

    # Open the CSV file and read its contents using DictReader
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)
        print(data)  # Print the loaded data for debugging purposes
        return data


def save_json_data(data, filename):
    """
    Save the provided data to a JSON file with pretty formatting (indent=2).
    """
    # Open the output file in write mode and dump the data as JSON
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        print(f"✅ Data saved to {filename}")


def preview_json_data(filename, count=3):
    """
    Load the JSON file and print the first 'count' entries for quick preview.
    Default preview count is 3 entries.
    """
    # Open the JSON file and load its contents
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        # Print the first 'count' entries with indentation for readability
        print(json.dumps(data[:count], indent=2))


def main():
    """
    Main function to orchestrate the CSV to JSON conversion process:
    1. Load data from the CSV file.
    2. Save the data to a JSON file.
    3. Preview the first few entries of the JSON file.
    """
    # Load data from the input CSV file
    data = load_csv_data(INPUT_FILE)
    # If no data is loaded, exit early
    if not data:
        print("No data to save.")
        return
    # Save the loaded data to the output JSON file
    save_json_data(data, OUTPUT_FILE)
    # Preview the first few entries of the saved JSON file
    preview_json_data(OUTPUT_FILE)


# Entry point of the script: run the main function when the script is executed directly
if __name__ == "__main__":
    main()
