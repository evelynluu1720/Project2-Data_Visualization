import plotly.express as px # type: ignore
import plotly.io as pio # type: ignore

from die import Die

# plotly plot opens on browser
pio.renderers.default = "browser"

# Create a D6 and a D10
die_1 = Die()
die_2 = Die(10)

# Make n_roll rolls, and store results in a list
results = []
n_roll = 50000

for i in range(n_roll):
    # Store sum of 2 rolls per time
    sum_roll = die_1.roll() + die_2.roll()
    results.append(sum_roll)

# Analyze the results
frequencies = []
# Find max result of sum of two rolls (in case each die has different number of sides)
max_result = die_1.num_sides + die_2.num_sides
possible_value = range(2, max_result +1)
for value in possible_value:
    # count how many times each possible value appear in list
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
title = 'Results of Rolling a D6 and a D10 50,000 times'
labels = {'x': 'Result', 'y': 'Frequency of Result'}

# bar(x value, y value) -> create a bar graph
fig = px.bar(
    x=possible_value, 
    y=frequencies,
    title = title,
    labels = labels
    )

# update_layout() -> make various updates to a figure after its been created
# xaxis_dtick -> distance between tick marks on x axis; spacing = 1 -> every bar is labeled
fig.update_layout(xaxis_dtick = 1)

# render resulting chart as an html file & open in browser tab
fig.show()

# to save chart as html file -> remove fig.show() and
# fig.write_html('dice_visual.xhtml')

'''
# Test for count() method

value1 = results.count(2)
print(value1)
print(results)
'''
