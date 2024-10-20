
DFW Air Quality Heatmap

Overview
This project generates a heatmap of air quality for various cities in the Dallas-Fort Worth (DFW) area. The heatmap is created using the folium library, with data retrieved from the OpenWeather API. Cities are color-coded based on their AQI (Air Quality Index), ranging from "Good" (green) to "Hazardous" (red).

Features
- Retrieves real-time AQI data for cities in the DFW area.
- Displays the data on an interactive map using a heatmap.
- Visualizes the air quality index with appropriate colors for easy understanding.

Files
- heatmap.py: Main Python script that fetches AQI data and generates the heatmap.
- dfw_cities.csv: CSV file containing the list of cities in the DFW area with their respective latitude and longitude values.

Setup Instructions

Prerequisites
- Python 3.x
- A valid API key from OpenWeather (https://openweathermap.org/api)

Dependencies
Install the required libraries using pip:
```bash
pip install requests pandas folium
```

CSV File
Ensure that the dfw_cities.csv file is in the same directory as the heatmap.py script. This file should contain the following columns:
- City: Name of the city.
- Latitude: Latitude of the city.
- Longitude: Longitude of the city.

Usage

1. Open the heatmap.py script.
2. Replace the placeholder API_KEY with your actual OpenWeather API key:
   ```python
   API_KEY = 'your_api_key_here'
   ```
3. Run the script:
   ```bash
   python heatmap.py
   ```
4. The script will fetch the AQI data for the listed cities and generate an interactive heatmap. The resulting HTML file will be saved in the same directory.

Example
Once the script is run, a file named air_quality_heatmap.html will be generated, displaying the air quality data for each city on the map.
