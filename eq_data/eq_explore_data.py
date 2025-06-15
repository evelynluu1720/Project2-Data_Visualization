from pathlib import Path
import json

import plotly.express as px # type: ignore
import plotly.io as pio # type: ignore

# plotly plot opens on browser
pio.renderers.default = "browser"

# Read data as a string & convert to a Python object
path = Path('eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text()
# convert string representation of file to Python object -> one dictionary
all_eq_data = json.loads(contents)

# # Create a more readable version of data life
# path = Path('eq_data/readable_eq_data.geojson')
# readable_contents = json.dumps(all_eq_data, indent=4)
# path.write_text(readable_contents)

# Examine all earthquakes in dataset
all_eq_dicts = all_eq_data['features'] # list of dictionaries
print(len(all_eq_dicts))

mags, longs, lats, eq_titles = [], [], [], []
for eq in all_eq_dicts:
    mag = eq['properties']['mag'] # extract magnitude by calling keys
    long = eq['geometry']['coordinates'][0]
    lat = eq['geometry']['coordinates'][1]
    eq_title = eq['properties']['title']

    mags.append(mag)
    longs.append(long)
    lats.append(lat)
    eq_titles.append(eq_title)

# Draw map
title = 'Global Earthquakes'
fig = px.scatter_geo(
    lat=lats, lon=longs, size=mags, title=title,
    color=mags,
    color_continuous_scale='Viridis',
    # set custom labels: change from label color to label Magnitude
    labels={'color':'Magnitude'},
    # modify shape of base map
    projection='natural earth',
    hover_name=eq_titles,
    )
fig.show()
