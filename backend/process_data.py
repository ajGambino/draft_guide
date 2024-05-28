import pandas as pd

# Read the existing CSV file
df_etr = pd.read_csv('etr.csv')

# Read the CSV file with weeks 15-17 and division info
df_weeks = pd.read_csv('weeks_15_17.csv')

# Merge the two DataFrames based on the "Team" column
df_merged = pd.merge(df_etr, df_weeks, on='Team')

# Rename the columns for weeks 15-17 and division
df_merged.rename(columns={
    'Week 17': 'Week_17',
    'Week 16': 'Week_16',
    'Week 15': 'Week_15',
    'Division': 'Division'
}, inplace=True)

# Add the new columns to the existing DataFrame
df_final = df_merged[['Team', 'Name', 'Position', 'ETR Rank', 'ADP', 'ADP Differential', 'Week_17', 'Week_16', 'Week_15', 'Division']]

# Save the DataFrame to a CSV file
df_final.to_csv('cheat_sheet.csv', index=False)
