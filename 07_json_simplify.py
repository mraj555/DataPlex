import os
import json

# Input and output file names
INPUT_FILE = "nested_data.json"
OUTPUT_FILE = "simplified_data.json"


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
    
    # If data is a list, iterate through its elements with index
    elif isinstance(data, list):
        for idx, item in enumerate(data):
            # Build the full key using the index as part of the key
            full_key = f"{parent_key}{sep}{idx}" if parent_key else str(idx)
            print(full_key)  # Debug: print the current key being processed
            # Recursively flatten each item and update items
            items.update(flatten_json(item, full_key, sep=sep))
    
    # If data is a primitive (string, number, etc.), add it to items
    else:
        items[parent_key] = data

    return items


def main():
    """
    Main function to load JSON, flatten it, and save the result.
    """
    # Check if the input file exists
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} does not exist.")
        return

    try:
        # Load the JSON data from the input file
        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # Prompt user for a custom separator, default to underscore
        sep = input("Enter separator (default: '_'): ") or "_"
        
        # Flatten the JSON data
        flattened_data = flatten_json(data, sep=sep)

        # Save the flattened data to the output file
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(flattened_data, f, indent=2)
            print(f"✅ Data saved to {OUTPUT_FILE}")
    
    # Catch and print any exceptions that occur
    except Exception as e:
        print(f"Error: {e}")
        return


# Entry point of the script
if __name__ == "__main__":
    main()
