This is a simple and powerful desktop GUI application built with Tkinter, Pandas, GeoPandas, and Matplotlib. It enables users to search for real estate properties by Zip Code or Latitude/Longitude and visualize the results on a real-world map using OpenStreetMap tiles.

✨ Features
🔍 Search by Zip Code or Latitude,Longitude

📌 Suggests the nearest zip code or coordinates if an exact match isn't found

🗺️ Interactive map of properties with price-based color gradient

📊 Summary statistics for filtered properties

🧾 Tabular view of property details

📘 Clear indication of available location ranges

🛠 Requirements
Install the required Python packages:

bash
Copy
Edit
pip install pandas matplotlib geopandas contextily shapely pyproj
If you're using Anaconda or run into issues installing geopandas and contextily, use:

bash
Copy
Edit
conda install geopandas contextily -c conda-forge
📁 Dataset Requirements
The application reads from a CSV file named your_property_data.csv placed in the same directory.

Required columns:


Column	Description
price	Price of the property
lat	Latitude of the property
long	Longitude of the property
zipcode	Zip code of the property
Each row should represent a single property listing.

▶️ How to Run
Ensure your dataset is named your_property_data.csv

Launch the application:

bash
Copy
Edit
python app.py
💡 Application Behavior
On startup, the app displays the available zip code and lat/lon ranges

The user can choose to search either by:

Zip Code (e.g., 98102)

Latitude,Longitude (e.g., 47.61,-122.33)

If no exact match is found:

A popup suggests the nearest matching zip code or coordinates

The entry field auto-fills with this suggestion

Results are shown in three tabs:

Summary – Basic statistical description

Charts – Interactive map colored by property price

Properties – Table of matching listings

🖼 Sample UI Screenshot
(Add a screenshot here named screenshot.png if desired)

📍 Note on Map Accuracy
Map tiles are pulled from OpenStreetMap

Coordinates are projected using Web Mercator (EPSG:3857)

The map may take a second or two to render depending on your internet connection

📄 License
MIT License – free for personal and commercial use.# Python-project-AVY
Course project of AAI-551C - Programming python - Real Estate study
