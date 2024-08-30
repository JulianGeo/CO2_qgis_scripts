import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from datetime import datetime

# Read the CSV file
csv_file = 'C:/Gis/data.csv' 

data = pd.read_csv(
    csv_file, 
    sep = ';', 
    encoding="unicode-escape",
    decimal=','
) 

data.head()

# Define a function to create LineString objects from coordinate pairs 

def create_line(row):
	return Point((row['X Coord'], row['Y Coord']))

# Apply the function to create a new 'geometry' column containing LineString objects 
data['geometry'] = data.apply(create_line, axis=1) 

# Convert the DataFrame to a GeoDataFrame and set the CRS 
gdf = gpd.GeoDataFrame(data, crs="EPSG:3116") 

# Save the GeoDataFrame as a shapefile 
date_string = datetime.datetime.today().strftime('%Y-%m-%d_%H-%M-%S')
output_shapefile = 'C:/Gis/data_'+date_string+'.shp' 
gdf.to_file(output_shapefile)

# Load the shp to the project
layer = iface.addVectorLayer(output_shapefile, '', 'ogr')

# Check if the layer was added successfully
if not layer:
    print("Error: Layer could not be added.")
else:
    print("Layer added successfully.")