import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

sales_filepath='../../data/2019_sales_by_month.xlsx'
brand_and_flag_filepath='../../data/hotel_brand_and_flag.xlsx' 
flag_groupings_filepath='../../data/flag-groupings.xlsx'
#read excel files for desired timeframe in pandas dataframes
sales_by_month = pd.read_excel(sales_filepath)
brand_and_flag = pd.read_excel(brand_and_flag_filepath)
flag_groupings = pd.read_excel(flag_groupings_filepath)

#format brand_and_flag
drop_na_brand = brand_and_flag.dropna(subset=['Property Code'])
brand_columns = ['Property Name', 'Brand', 'Flag', 'Property Code', '#Rooms']
current_hotel_brand_and_flags = drop_na_brand[brand_columns].copy()

#clean flag column
current_hotel_brand_and_flags['Flag'].replace(to_replace='Hampton Inn & Suites', value='Hampton Inn & Suites by Hilton', inplace=True)
current_hotel_brand_and_flags['Flag'].replace(to_replace='Hampton Inn', value='Hampton Inn by Hilton', inplace=True)
current_hotel_brand_and_flags['Flag'].replace(to_replace='Embassy Hilton', value='Embassy Suites', inplace=True)
current_hotel_brand_and_flags['Flag'].replace(to_replace='DoubleTree', value='DoubleTree by Hilton', inplace=True)
current_hotel_brand_and_flags['Flag'].replace(to_replace='avid an IHG hotel', value='Avid Hotels', inplace=True)
current_hotel_brand_and_flags['Flag'].replace(to_replace='Holiday Inn', value='Holiday Inn Hotels & Resorts', inplace=True)
current_hotel_brand_and_flags['Flag'].replace(to_replace='Hilton Full Service', value='Hilton Hotels & Resorts', inplace=True)
current_hotel_brand_and_flags['Flag'].replace(to_replace='EVEN', value='Even Hotels', inplace=True)
current_hotel_brand_and_flags['Flag'].replace(to_replace='Intercontinental Hotels', value='InterContinental', inplace=True)

#create performance dataframe with desired columns
drop_na = sales_by_month.dropna(subset=['Property Code'])
performance_columns = ['Property Name', 'Property Code', 'Brand', '#Rooms', 'Activation Date', 'Revenue', 'Profit Margin', 'Gross Profit']
performance_df = drop_na[performance_columns].copy()

#clean up brand column
performance_df['Brand'].replace(to_replace=['Tru B', 'TRU B', 'TRU b', 'Tru b', 'Home2', 'Homew', 'The S', 'Hampt', 'Doubl', 'Embas', 'Miram'], value='Hilto', inplace=True)
performance_df['Brand'].replace(to_replace=['Stayb', 'Inter', 'IHG A', 'Holid', 'Avid ', 'Crown', 'Candl'], value='IHG', inplace=True)
performance_df['Brand'].replace(to_replace= ['Aston', 'Delta', 'Renai'], value='Marri', inplace=True)
performance_df['Brand'].replace(to_replace= ['Quali', 'Comfo'], value='Choic', inplace=True)
performance_df['Brand'].replace(to_replace= 'La Qu', value='Wyndh', inplace=True)
performance_df['Brand'].replace(to_replace= ['Blueb', 'River'], value='Apart', inplace=True)
performance_df['Brand'].replace(to_replace= ['Platt'], value='Impul', inplace=True)
performance_df['Brand'].replace(to_replace= ['Hammo'], value='Indep', inplace=True)

arr = ['LAXMA', 'LGBMY']
prop_mask1 = performance_df['Property Code'].isin(arr) 
performance_df['Brand'][prop_mask1] = 'Hilto'
prop_mask2 = performance_df['Property Code'] == 'IHG - ATLID'
performance_df['Brand'][prop_mask2] = 'IHG'

#create flag
property_code_column = list(performance_df['Property Code'])
flag_column = []
for code in property_code_column:
    flag = current_hotel_brand_and_flags.loc[current_hotel_brand_and_flags['Property Code'] == code, 'Flag'].iat[0]
    flag_column.append(flag)
performance_df['Flag'] = flag_column

#add size subset columns
num_rooms_column = list(performance_df['#Rooms'])
size_subset = []
for num_rooms in num_rooms_column:
    if num_rooms <= 0:
        size_subset.append(0) 
    elif 0 < num_rooms < 80:
        size_subset.append(1)
    elif 80 <= num_rooms < 100:
        size_subset.append(2)
    elif 100 <= num_rooms < 150:
        size_subset.append(3)
    elif 150 <= num_rooms < 200:
        size_subset.append(4)
    else:
        size_subset.append(5)

performance_df['Size Subset'] = size_subset

#create SPOR columns
avg_occupancy = 0.68 #industry average
SPOR = [performance_df['Revenue']/(performance_df['#Rooms']*30.62*avg_occupancy)]
SPOR_df = pd.DataFrame(SPOR).transpose()
performance_df['SPOR'] = SPOR_df

#create group and type columns
group_column = []
type_column = []
industry_flags = list(flag_groupings['Flag'])
for prop_flag in flag_column:
    if prop_flag in industry_flags:
        group = flag_groupings.loc[flag_groupings['Flag'] == prop_flag, 'Group'].iat[0]
        hotel_type = flag_groupings.loc[flag_groupings['Flag'] == prop_flag, 'Type'].iat[0]
    else:
        group = 'Other'
        hotel_type = 'Other'
    group_column.append(group)
    type_column.append(hotel_type)
performance_df['Group'] = group_column
performance_df['Type'] = type_column
performance_df



#drop all hotels with activation date after 2019-01-01
m1 = performance_df['Activation Date'] <= '2019-01-01'

#drop all hotels wtih a profit margin > 0.74 or < 0.44
m2 = performance_df['Profit Margin'] < 0.74
m3 = performance_df['Profit Margin'] > 0.44
comparison_hotels = performance_df[m1 & m2 & m3].copy()

comparison_hotels.to_csv('../data/clean-sales-data.csv', index = False)

if __name__ == "__main__":
    sales_filepath='../../data/2019_sales_by_month.xlsx'
    brand_and_flag_filepath='../../data/hotel_brand_and_flag.xlsx' 
    flag_groupings_filepath='../../data/flag-groupings.xlsx'
