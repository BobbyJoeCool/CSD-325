import csv
from datetime import datetime

from matplotlib import pyplot as plt

print("Hello!  This program will show you a graph of the high or "
        "low temperatures in Sitka, Alaska over the 2018 Year.  "
        "Please select from the menu which graph you would like to see."
        "Enter 'exit' to exit the program."
    )

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
    # Added getting low temps as a list
        low = int(row[6])
        lows.append(low)

# Create fucntions to plot the temperatures.
# Uses functions so a composite graph can be made calling both.
#plt.style.use('seaborn')
def plotHighs(ax):
    ax.plot(dates, highs, c='red')

def plotLows(ax):
    ax.plot(dates, lows, c='blue')

while True: # Enters a while loop so the user can keep asking for graphs until they choose to exit.
    userSelection = input(f"\nMain Menu\n"
            "1) Display High Temperatures\n"
            "2) Display Low Temperatures\n"
            "3) Display Both Together\n"
            "Enter your Selection or type 'exit' to quit: "
            )
    
    if userSelection.lower() == "exit":
        print("\nThanks for using the Daily Temperature Plot Program.")
        break

    if userSelection not in ["1", "2", "3"]: # ensures choice input
        print("\nInvalid Selection, please select again.")
        continue

    fig, ax = plt.subplots()

    if userSelection == "1":
        programType = "Daily High Temperatures"
        plotHighs(ax)

    if userSelection == "2":
        programType = "Daily Low Temperatures"
        plotLows(ax)

    if userSelection == "3":
        programType = "Daily High and Low Temperatures"
        plotHighs(ax)
        plotLows(ax)

    # Format plot.
    plt.title(f"{programType}", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()