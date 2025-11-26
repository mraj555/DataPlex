import os          # Provides functions for interacting with the operating system (e.g., checking file existence)
import json        # Handles JSON encoding and decoding
import csv         # Handles CSV file reading and writing

# --- Configuration Constants ---
INPUT_FILE = "api_data.json"      # Path to the source JSON file
OUTPUT_FILE = "converted_data.csv"  # Path where the resulting CSV will be saved


def load_json_data(filename):
    """
    Load and return JSON data from the specified file.

    If the file does not exist or contains invalid JSON, an empty list is returned
    and an appropriate message is printed.
    """
    # Check if the JSON file exists on disk
    if not os.path.exists(filename):
        print("No Json file found.")
        return []

    # Open and attempt to parse the JSON file
    with open(filename, "r", encoding="utf-8") as f:
        try:
            return json.load(f)  # Convert JSON text into Python objects (list/dict)
        except:
            print("Invalid JSON format.")
            return []


def save_csv_data(data, filename):
    """
    Save a list of dictionaries to a CSV file.

    Each dictionary in the list becomes a row; keys become column headers.
    """
    # Guard clause: do nothing if there's no data
    if not data:
        print("No data to save.")
        return

    # Open the output CSV file for writing
    with open(filename, "w", newline="", encoding="utf-8") as f:
        # Create a CSV writer that uses dictionary keys as fieldnames
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()  # Write the column headers

        # Iterate over each dictionary (row) and write it to the CSV
        for record in data:
            writer.writerow(record)

        print(f"Data successfully saved to {filename}")


def main():
    """Main entry point: orchestrates the JSON-to-CSV conversion."""
    print("Starting JSON to CSV conversion...")
    
    # Step 1: Load JSON data from the input file
    data = load_json_data(INPUT_FILE)
    
    # Step 2: If data was loaded successfully, save it as CSV
    if data:
        save_csv_data(data, OUTPUT_FILE)
    else:
        print("No data to convert.")


# Run the main function only when this script is executed directly
if __name__ == "__main__":
    main()
