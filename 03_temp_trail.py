# Import standard libraries for file handling, CSV operations, date/time, and HTTP requests
import os
import csv
from datetime import datetime
import requests

# Configuration constants
FILENAME = "weather.csv"  # Name of the CSV file where weather logs are stored
API_KEY = "Enter your OpenWeatherMap API key here"  # OpenWeatherMap API key

# Create (or overwrite) the CSV file and write the header row
with open(FILENAME, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Date", "City", "Temperature", "Condition"])


def log_weather():
    """
    Prompt the user for a city name, fetch current weather data from OpenWeatherMap,
    and append the data to the CSV file if it hasn't already been logged today.
    """
    # Get today's date in YYYY-MM-DD format
    date = datetime.now().strftime("%Y-%m-%d")
    city = input("Enter your city name: ").strip()

    # Check if this city has already been logged today
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Date"] == date and row["City"].lower() == city.lower():
                print("This city has already been logged for today.")
                return

    # Build the API URL with the city name, API key, and metric units
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        # Handle non-200 HTTP status codes
        if response.status_code != 200:
            print(f"Error: {data.get('message', 'Unknown error')}")
            return

        # Extract temperature and weather condition from the JSON response
        temp = data["main"]["temp"]
        condition = data["weather"][0]["main"]

        # Display the weather info to the user
        print(f"🌤️ Temperature in {city} on {date}: {temp}°C — {condition} 🌈")
        # Append the new log entry to the CSV file
        with open(FILENAME, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([date, city, temp, condition])
    except Exception as e:
        # Catch any exceptions (network issues, parsing errors, etc.)
        print(f"Error fetching weather data: {e}")
        return


def view_logs():
    """
    Read and display all weather logs stored in the CSV file.
    If the file doesn't exist or is empty (only header), inform the user.
    """
    if not os.path.exists(FILENAME):
        print("No Weather Logs Found.")
        return

    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = list(csv.reader(f))

        # Check if only the header row exists
        if len(reader) <= 1:
            print("No Weather Logs Found.")
            return

        # Print a simple table of logs
        print("-" * 50)
        for row in reader[1:]:
            print(f" {row[0]} | {row[1]} | {row[2]} | {row[3]} ")
        print("-" * 50)


def main():
    """
    Main menu loop for the Real Time Weather Logger.
    Provides options to add a log, view logs, or exit.
    """
    while True:
        print("Real Time Weather Logger 🌡️")
        print("1. Add Weather Log")
        print("2. View All Weather Logs")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        match choice:
            case "1":
                log_weather()
            case "2":
                view_logs()
            case "3":
                print("Exiting the program. Goodbye! 👋")
                break
            case _:
                print("Invalid choice. Please enter a number between 1-3.")


# Run the main function only when this script is executed directly
if __name__ == "__main__":
    main()
