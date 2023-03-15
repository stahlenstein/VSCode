import simplekml
import pandas as pd

# create a dictionary of the folders and their associated routes
folders = {
    'Silver Creek': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 23, 24, 25, 26, 27, 28, 29],
    'Lindale': [21, 22, 30, 31, 32, 33],
    'Kingston': [42, 43, 44, 45, 46, 47],
    'Shannon': [50, 51, 52, 53, 61, 62],
    'Armuchee': [68, 69, 70, 71, 72, 73, 74, 75, 77, 78, 79, 88],
    'Coosa': [80, 81, 82, 83, 84, 85, 91]
}

# read in the Excel file using pandas
df = pd.read_excel(r'C:\Users\Marvin\Documents\VSCode\Python\Kml\GPS.xlsx')

# convert the "Account Number" column to string values
df['Account Number'] = df['Account Number'].astype(pd.StringDtype())

# Remove deciaml and decimal numerical value from the "Account Number" column
df['Account'] = df['Account Number'].str.replace(".0", "", regex=False)

# add leading zeros to 'Account' column
df['Account'] = df['Account'].apply('{:0>6}'.format)

# create a kml object
kml = simplekml.Kml(visibility= 0)

# Adding the screen overlay 
screen = kml.newscreenoverlay(name='Panel')
screen.icon.href = 'https://raw.githubusercontent.com/stahlenstein/Map_Beta/main/images/logo.png'
screen.overlayxy = simplekml.OverlayXY(x=0,y=1,xunits=simplekml.Units.fraction, yunits=simplekml.Units.fraction)
screen.screenxy = simplekml.ScreenXY(x=25,y=25,xunits=simplekml.Units.pixels, yunits=simplekml.Units.insetpixels)
screen.size.x = 0
screen.size.y = 0
screen.size.xunits = simplekml.Units.fraction
screen.size.yunits = simplekml.Units.fraction

# iterate over each folder in the dictionary
for folder_name, folder_routes in folders.items():
    # create a folder for the current folder name
    kml_folder = kml.newfolder(name=folder_name)
    # iterate over each route number in the current folder
    for route in folder_routes:
        # create a folder for the current route number
        route_folder = kml_folder.newfolder(name=str(route))
        # iterate over each row in the dataframe where the route number matches the current route

        for index, row in df[df['Route'] == route].iterrows():
            # create a placemark with the latitude, longitude, and name from the dataframe
            placemark = route_folder.newpoint(name= row['Address'], description=(f"\n Account #: {row['Account']} \n Meter #: {row['Meter Number']} \n Route: {row['Route']} \n"), coords=[(row['Longitude'], row['Latitude'])])

kml.save('meters.kml')