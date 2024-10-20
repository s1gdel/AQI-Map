import requests
import pandas as pd
import folium
from folium.plugins import HeatMap

# Set your OpenWeather API key here
API_KEY = '6697398c7eb365695310277073455631'

# Load the cities from the CSV file
df = pd.read_csv('dfw_cities.csv')  # Make sure the CSV file is in the same directory

# AQI to color mapping (Green to Red scale)
def get_color(aqi):
    if aqi == 1:
        return 'green'     # Good
    elif aqi == 2:
        return 'yellow'    # Fair
    elif aqi == 3:
        return 'orange'    # Moderate
    elif aqi == 4:
        return 'red'       # Poor
    elif aqi == 5:
        return 'purple'    # Very Poor
    else:
        return 'gray'      # Unknown

# Fetch air quality data for each location
def get_AQ(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data['list'][0]['main']['aqi']  # Air Quality Index (1-5 scale)

# Create a map centered around DFW
dfw_map = folium.Map(location=[32.7767, -96.7970], zoom_start=9)

# Iterate through each city in the dataset
for index, row in df.iterrows():
    city_name = row['name']
    lat = row['lat']
    lon = row['lon']
    
    # Get AQI for the current city
    aqi = get_AQ(lat, lon)
    color = get_color(aqi)

    # Add circle markers to the map with AQI color
    folium.CircleMarker(
        location=[lat, lon],
        radius=15,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.15,
        popup=f"{city_name} - AQI: {aqi}"
    ).add_to(dfw_map)

# Add legend (color-coded for AQI)
legend_html = """
<div style="position: fixed;
     bottom: 50px; left: 50px; width: 150px; height: 120px;
     background-color: white; border:2px solid grey; z-index:9999;
     font-size:14px;">
     &nbsp; <b>AQI Scale</b> <br>
     &nbsp; <i style="background:green;color:white;padding:3px;">Good (1)</i><br>
     &nbsp; <i style="background:yellow;color:black;padding:3px;">Fair (2)</i><br>
     &nbsp; <i style="background:orange;color:black;padding:3px;">Moderate (3)</i><br>
     &nbsp; <i style="background:red;color:white;padding:3px;">Poor (4)</i><br>
     &nbsp; <i style="background:purple;color:white;padding:3px;">Very Poor (5)</i><br>
</div>
"""

dfw_map.get_root().html.add_child(folium.Element(legend_html))

# Save map as HTML file
dfw_map.save("DFWAQ_Heatmap.html")

print("DFW Air Quality Heatmap with AQI scale has been generated and saved as DFWAQ_Heatmap.html.")
