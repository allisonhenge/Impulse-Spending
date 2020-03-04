import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

flag_groupings = pd.read_excel('../../data/flag-groupings.xlsx')

# create brand_and_flags dictionary, brand:flags, dropdown #1 : dependant dropdown #2
unique_brands = list(flag_groupings['Brand'].unique()) + ['Other', 'Retail', 'Apartment']

def get_brand_flags(brand):
    brand_flags_mask = flag_groupings['Brand'] == brand
    brand_df = flag_groupings[brand_flags_mask]
    brand_unique_flags = list(brand_df['Flag'].unique()) + ['Other']
    return brand_unique_flags

brand_and_flags = {}
for brand in unique_brands:
    brand_and_flags[brand] = get_brand_flags(brand)

specialty_service = ['None', 'Airport', 'Convention Center']
revenue_period = ['Yearly', 'Quarterly', 'Monthly']
profit_type = ['Current Profit', 'Profit Margin']

create_cust_options = [brand_and_flags, specialty_service, revenue_period, profit_type]




