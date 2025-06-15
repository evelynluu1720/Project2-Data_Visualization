from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# path = Path('weather_data/sitka_weather_07-2021_simple.csv')
path = Path('weather_data/sitka_weather_2021_simple.csv')
# get list of all lines
lines = path.read_text().splitlines() # type list

# create reader object, used to parsed lines later
reader = csv.reader(lines)
# reader = csv.reader(path) -> path: Posix Path object, not iterable
# next() -> return next line infile, here we call once -> get first line == header
header_row = next(reader)
# print(lines[:2])

# enumerate() -> returns both index and value of each item as looping through a list
# for index, header in enumerate(header_row):
#     print(index, header)
# -> index dates = 2; index high temp = 4

# Extract dates & high temp of each row
dates, highs, lows = [], [], []
'''
reason for using reader and not lines:
- lines are list of lines, in which each line is a string that concatenates all values -> hard to extract just high temp
- reader is an reader object that we have read its first row (header) using next() -> now it will loop from second row onwards
'''
for row in reader:
    high = int(row[4]) # high temp index = 4
    low = int(row[5])
    # convert string to datetime object
    date = datetime.strptime(row[2], '%Y-%m-%d')

    highs.append(high)
    lows.append(low)
    dates.append(date)

# Plot high & low temp
plt.style.use('ggplot')
fig, ax = plt.subplots()

# Plot line chart, each code line = 1 line chart
# alpha: color transparency: 0-transparent to 1-opaque
ax.plot(dates, highs, color = 'red', alpha=0.5)
ax.plot(dates, lows, color = 'blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
ax.set_title('Daily High and Low Temperatures, 2021', fontsize = 24)
ax.set_xlabel('', fontsize = 16)
# draw date labels diagonally so that they wont overlap
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize = 16)
ax.tick_params(labelsize = 16)

plt.show()