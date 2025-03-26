
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from datetime import datetime
from qgis.core import QgsProject
from config import *
import os

# Define a function to create LineString objects from coordinate pairs 

def create_point(row):
	return Point((row[x_coord_name], row[y_coord_name]))


def get_project_directory():
    project = QgsProject.instance()
    project_path = project.fileName()

    if project_path:
        pwd = os.path.dirname(project_path)
        print('project directory:',pwd)
        return pwd
    else:
        return None

def convert_csv_2_shp(
    csv_path,
    output_file_path,
    dataType,
):
    
    # Read the CSV file   
    data = pd.read_csv(
        csv_path, 
        sep = separator, 
        encoding="unicode-escape",
        decimal=decimal
    )

    data.head()

    # Apply the function to create a new 'geometry' column containing Point objects 
    data['geometry'] = data.apply(create_point, axis=1) 

    # Convert the DataFrame to a GeoDataFrame and set the CRS 
    gdf = gpd.GeoDataFrame(data, crs=crs) 
    date_string = datetime.today().strftime('%Y-%m-%d_%H-%M-%S')

    # Save the GeoDataFrame as a shapefile 
    #output_shapefile = output_file_path +'/'+dataType+'_'+date_string+'.shp' 
    output_shapefile = os.path.join(
        get_project_directory(), 
        output_file_path, 
        dataType+date_string+'.shp' 
    )
    
    gdf.to_file(output_shapefile)

    return output_shapefile
