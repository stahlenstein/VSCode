import pandas as pd

# Load the FCWD and Parcels Excel files into dataframes
fcwd = pd.read_excel('GPS1_NO ZEROES_ EDITED.xlsx')
parcels = pd.read_excel('Parcels_NO ZEROES.xlsx')

# Merge the two dataframes on the 'Address' column
merged = pd.merge(fcwd, parcels, on='Address', how='outer', copy=True, indicator=True, suffixes=('_fcwd', '_parcels'))

# Save the merged dataframe to a new Excel file
merged.to_excel('Merged_NO ZEROES_05.xlsx', index=False)
