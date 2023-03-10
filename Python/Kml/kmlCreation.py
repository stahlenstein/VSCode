import pandas as pd
import simplekml

# read data from Excel file
df = pd.read_excel('GPS Addresses Full lat_long.xlsx')

# create KML object
kml = simplekml.Kml()

# iterate over rows and create placemarks
for index, row in df.iterrows():
    # extract data from row
    name = row['Address']
    description = row['Account Number']
    longitude = row['Longitude']
    latitude = row['Latitude']

    # create placemark with data from row
    placemark = kml.newpoint(name=name, description=description, coords=[(longitude, latitude)])

# save KML file
kml.save('output.kml')
