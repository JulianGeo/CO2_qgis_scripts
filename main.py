"""
This script converts CSV data into a shapefile and visualizes it in QGIS with specific styling based on the data type.

Dependencies:
- QGIS Python API
- Custom `csv_data_2_shp` module
- Configuration file (`config.py`)
"""

from csv_data_2_shp import convert_csv_2_shp
from qgis.core import  QgsSimpleMarkerSymbolLayer
from config import *

new_shape = convert_csv_2_shp(
    csv_file_path,
    output_folder,
    data_type
)


layer = iface.addVectorLayer(new_shape, data_type, 'ogr')


if data_type == 'TERMALES':
    
    marker_layer = QgsSimpleMarkerSymbolLayer()
    marker_layer.setShape(QgsSimpleMarkerSymbolLayer.DiamondStar)
    
    symbol = layer.renderer().symbol()
    symbol.appendSymbolLayer(marker_layer)
    symbol.deleteSymbolLayer(0)
    symbol.setColor(QColor(232, 39, 141))
    symbol.setSize(symbol_size)
    layer.triggerRepaint()
else:
    layer.renderer().symbol().setColor(QColor(255,87,51))
    layer.triggerRepaint()


# Check if the layer was added successfully
if not layer:
    print("Error: Layer could not be added.")
else:
    print("Layer added successfully.")