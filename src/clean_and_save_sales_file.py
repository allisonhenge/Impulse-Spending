import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import openpyxl
pd.options.mode.chained_assignment = None

import matplotlib
import matplotlib.pyplot as plt

sales_filepath='../../data/2019_sales_by_month.xlsx'
brand_and_flag_filepath='../../data/hotel_brand_and_flag.xlsx' 
flag_groupings_filepath='../data/flag_groupings.xlsx'
#read excel files for desired timeframe in pandas dataframes
sales_by_month = pd.read_excel(sales_filepath)
brand_and_flag = pd.read_excel(brand_and_flag_filepath)
flag_groupings = pd.read_excel(flag_groupings_filepath)

#format brand_and_flag
brand_and_flag.dropna(subset=['Property Code'])
brand_columns = ['Property Name', 'Brand', 'Flag', 'Property Code', '#Rooms']
current_hotel_brand_and_flags = brand_and_flag[brand_columns].copy()

#create performance dataframe with desired columns
sales_by_month.dropna(subset=['Property Code'])
performance_columns = ['Property Name', 'Property Code', 'Brand', '#Rooms', 'Activation Date', 'Revenue', 'Profit Margin', 'Gross Profit']
performance_df = sales_by_month[performance_columns].copy()

#add flag and SPOR columns
property_code_column = list(performance_df['Property Code'])
flag_column = []
for code in property_code_column:
    flag = current_hotel_brand_and_flags.loc[current_hotel_brand_and_flags['Property Code'] == code, 'Flag'].iat[0]
    flag_column.append(flag)
performance_df['Flag'] = flag_column

avg_occupancy = 0.68 #industry average
SPOR = [performance_df['Revenue']/(performance_df['#Rooms']*30.62*avg_occupancy)]
SPOR_df = pd.DataFrame(SPOR).transpose()
performance_df['SPOR'] = SPOR_df

# unique_flags = list(current_hotel_brand_and_flags['Flag'].unique())

# def get_brand_flags(brand):
#     brand_flags_mask = flag_groupings['Brand'] == brand
#     brand_df = flag_groupings[brand_flags_mask]
#     brand_unique_flags = list(brand_df['Flag'].unique()) + ['Other']
#     return brand_unique_flags

# brand_and_flags = {}
# for brand in unique_brands:
#     brand_and_flags[brand] = get_brand_flags(brand)
'''
reassign brands/flags add location  
remove all unnecessary columns
create SPOR
'''
'''
customer input 
#1 - Brand dropdown limited to 7 large brands, independant and retail
    -Hilton/IHG do comparisions within brand unless its better compared with each other dependant on location type
    -Marriott/Choice/Wyndham/BestWestern/Independant all compared to a similar Hilton or IHG flag
    -Apartment and Retail link straight to a email prompt
#2 - Flag *dropdown dependant on dropdown #1. INCLUDE sub-flags where needed as separate type
    -unless specified compare within similar flags under brand. There will be some cross-linked between brands
#3 - Number of rooms
    -will need to have a for loop for size specification... then +/- 10% for neighbors
#4 - Location type dropdown independant(limit to major differences)
    -luxury/select service/airport/convention center/full service/ etc
#5 - average occupancy
    -if not entered assume 68% as industry average
#6 - current retail space profit or profit margin. 
    -will need to have a dropdown for input type and then a field for entry
#7 - 
'''

'''
what the script needs to do

calculate SPOR/ ROI? etc
auto generate message containing all hotel information plus calculations to impulsify
return SPOR and PM to customer on dashboard

'''


#comparison_df = df.to_csv(r'../../data/clean_sales_data.csv', index = False)

if __name__ == "__main__":
    sales_filepath='../../data/2019_sales_by_month.xlsx'
    brand_and_flag_filepath='../../data/hotel_brand_and_flag.xlsx' 
    flag_groupings_filepath='../data/flag_groupings.xlsx'
