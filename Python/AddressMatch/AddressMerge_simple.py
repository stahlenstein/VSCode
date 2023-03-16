import pandas as pd

# read in the FCWD and Parcels Excel files
fcwd_df = pd.read_excel('GPS.xlsx')
parcels_df = pd.read_excel('Parcels.xlsx')

# merge the two dataframes based on the 'address' column
merged_df = pd.merge(fcwd_df, parcels_df, on='Address', how='outer')

# write the merged dataframe to a new Excel file
merged_df.to_excel('Merged.xlsx', index=False)

