from pyproj import Proj, transform

# Define the source and target coordinate systems
src_proj = Proj(init='epsg:25832')
tgt_proj = Proj(init='epsg:4326')

# Your original coordinates
x, y = 396641.64421609195, 6738668.986143405

# Convert the coordinates
lon, lat = transform(src_proj, tgt_proj, x, y)

print(f'Latitude: {lat}, Longitude: {lon}')