from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines() # create list of lines

reader = csv.reader(lines) # create reader object
header_row = next(reader)

# for index, header in enumerate(header_row):
#     print(index, header)

dates, highs, lows = [], [], []

for row in reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f'Missing data for {date}')
    else:
        dates.append(date)
        highs.append(high)
        lows.append(low)

# Plot

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, color='blue', alpha=0.1)

ax.set_title('Daily High and Low Temperatures, 2021\nDeath Valley, CA', fontsize=20)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('', fontsize=16)