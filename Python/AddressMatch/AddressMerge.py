import pandas as pd
from fuzzywuzzy import fuzz

# read in the FCWD and Parcels Excel files
fcwd_df = pd.read_excel('GPS.xlsx')
parcels_df = pd.read_excel('Parcels.xlsx')

# convert the 'address' column to strings
fcwd_df['Address'] = fcwd_df['Address'].astype(str)
parcels_df['Address'] = parcels_df['Address'].astype(str)

# define a function to get the closest matching address from parcels_df for a given address
def get_closest_address(address, addresses):
    best_score = -1
    best_match = None
    for a in addresses:
        score = fuzz.ratio(address, a)
        if score > best_score:
            best_score = score
            best_match = a
    return best_match

# add a new column to FCWD dataframe with the closest matching address from parcels_df
fcwd_df['closest_address'] = fcwd_df['Address'].apply(get_closest_address, args=[parcels_df['Address'].tolist()])

# merge the two dataframes based on the 'closest_address' column
merged_df = pd.merge(fcwd_df, parcels_df, left_on='closest_address', right_on='address', how='outer')

# drop the 'closest_address' column from the merged dataframe
merged_df.drop('closest_address', axis=1, inplace=True)

# write the merged dataframe to a new Excel file
merged_df.to_excel('Merged.xlsx', index=False)
