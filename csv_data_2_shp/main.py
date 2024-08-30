from csv_data_2_shp import convert_csv_2_shp

new_shape = convert_csv_2_shp(
    'C:/Gis/data.csv', 
    'C:/Gis/GIS_Backup/DATA/data',
)


layer = iface.addVectorLayer(new_shape, '', 'ogr')

# Check if the layer was added successfully
if not layer:
    print("Error: Layer could not be added.")
else:
    print("Layer added successfully.")