import csv                       # Read CSV files
from collections import defaultdict  # Auto-creates dictionary entries with default int(0)
import matplotlib.pyplot as plt  # Plotting library

# Name of the CSV file containing weather data
FILENAME = "weather.csv"


def visualize_weather():
    # Lists to store dates and temperatures for the line chart
    dates = []
    temps = []
    # Dictionary to count how many times each weather condition occurs
    conditions = defaultdict(int)

    # Open the CSV file safely with UTF-8 encoding
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)  # Reads rows as dictionaries using header row

        # Loop through each row in the CSV
        for row in reader:
            try:
                # Collect date and temperature; convert temperature to float
                dates.append(row["Date"])
                temps.append(float(row["Temperature"]))
                # Increment the count for this weather condition
                conditions[row["Condition"]] += 1
            except Exception as e:
                # Skip rows with missing or invalid data
                continue

    # Create and display a line chart of daily temperatures
    plt.figure(figsize=(10, 7))          # Set figure size (width, height) in inches
    plt.plot(dates, temps, marker="o")  # Plot temperature vs date with circle markers
    plt.title("Daily Temperature Trends")  # Chart title
    plt.xlabel("Date")                   # X-axis label
    plt.ylabel("Temperature (°C)")       # Y-axis label
    plt.tight_layout()                   # Adjust spacing to prevent label overlap
    plt.grid(True)                       # Enable grid lines for easier reading
    plt.show()                           # Display the chart

    # Create and display a bar chart of weather condition frequencies
    plt.figure(figsize=(7, 5))
    plt.bar(conditions.keys(), conditions.values(), color="skyblue")
    plt.xlabel("Weather Condition")
    plt.ylabel("Frequency")
    plt.show()


# Run the visualization only when this script is executed directly
if __name__ == "__main__":
    visualize_weather()
