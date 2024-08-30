
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from datetime import datetime

# Define a function to create LineString objects from coordinate pairs 

def create_point(row):
	return Point((row['X Coord'], row['Y Coord']))

def convert_csv_2_shp(
    csv_path,
    output_file_path
):
    
    # Read the CSV file   
    data = pd.read_csv(
        csv_path, 
        sep = ';', 
        encoding="unicode-escape",
        decimal=','
    )

    data.head()

    # Apply the function to create a new 'geometry' column containing Point objects 
    data['geometry'] = data.apply(create_point, axis=1) 

    # Convert the DataFrame to a GeoDataFrame and set the CRS 
    gdf = gpd.GeoDataFrame(data, crs="EPSG:3116") 
    date_string = datetime.today().strftime('%Y-%m-%d_%H-%M-%S')

    # Save the GeoDataFrame as a shapefile 
    output_shapefile = output_file_path +date_string+'.shp' 
    gdf.to_file(output_shapefile)

    return output_shapefile
