# Python Crash Course 2e
# Exercise 16.1

# sitka_rainfall

import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "data/sitka_weather_2018_simple.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates = []
    p_rates = []

    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        p_rate = float(row[3])
        p_rates.append(p_rate)
        dates.append(current_date)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, p_rates, c='blue')

ax.set_title("Daily Precipitation Rates - 2018", fontsize=24)
ax.set_xlabel("", fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel("Precipitation Rate (%)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize = 16)

plt.show()

# PRCP is located at index 3 (row[3])
# PRCP values are float
