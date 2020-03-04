import numpy as np
import pandas as pd

from pandas import ExcelWriter
from pandas import ExcelFile

flag_groupings = pd.read_excel('../../../data/flag-groupings.xlsx')
clean_sales_data = pd.read_csv('../../data/clean_sales_data.csv')

def get_comparison_df(brand, flag, size_subset, hotel_type, hotel_group):
    if brand == 'Not Hotel':
        comparison_df = 'Not Hotel Data'
    elif brand == 'Hilto':
        brand_mask = clean_sales_data['Brand'] == 'Hilto'
        brand_df = clean_sales_data[brand_mask].copy()
        flag_mask = brand_df['Flag'] == flag
        size_mask = brand_df['Size Subset'] == size_subset
        flag_df = brand_df[flag_mask & size_mask].copy()
        if len(flag_df) > 8:
            hilton_comparison_df = flag_df.copy()
        elif len(flag_df) <= 8:
            type_mask = brand_df['Type'] == hotel_type
            group_mask = brand_df['Group'] == hotel_group
            hilton_comparison_df = brand_df[type_mask & group_mask & size_mask].copy()
        comparison_df = hilton_comparison_df.copy()
    elif brand == 'IHG':
        brand_mask = clean_sales_data['Brand'] == 'IHG'
        brand_df = clean_sales_data[brand_mask].copy()
        flag_mask = brand_df['Flag'] == flag
        size_mask = brand_df['Size Subset'] == size_subset
        flag_df = brand_df[flag_mask & size_mask].copy()
        if len(flag_df) > 8:
            IHG_comparison_df = flag_df.copy()
        elif len(flag_df) <= 8:
            type_mask = brand_df['Type'] == hotel_type
            group_mask = brand_df['Group'] == hotel_group
            IHG_comparison_df = brand_df[type_mask & group_mask & size_mask].copy()
        comparison_df = IHG_comparison_df.copy()
    else:
        type_mask = clean_sales_data['Type'] == hotel_type
        group_mask = clean_sales_data['Group'] == hotel_group
        size_mask = clean_sales_data['Size Subset'] == size_subset
        other_brands_comparison_df = clean_sales_data[type_mask & group_mask & size_mask].copy()
        comparison_df = other_brands_comparison_df
    return comparison_df

comparison_df = get_comparison_df(brand, flag, size_subset, hotel_type, hotel_group)

def compare_data(comparison_df, customer_inputs):
    if comparison_df == 'Not Hotel Data' or revenue == 'No Current Retail Revenue' or \
        profit_margin == 'Not Currently Profitable' or \
        hotel_group == 'Not Hotel' or hotel_type == 'Not Hotel':
        results = "Our robot could not compare your data to enough similar hotels to be accurate. \
        That just means we get to contact you directly through the email you've provided"
    else:
        results = 'Placeholder'
    return results

# def get_comparison_results():


if __name__ == "__main__":
    name = 'The Make Believe Hampton'
    brand = 'Hilto'
    flag = 'Hampton Inn by Hilton'
    num_rooms = 303
    room_range = [273, 333]
    size_subset = 5
    hotel_type = 'Focused Service'
    hotel_group = 'Select Service'
    specialty_service = 'None'
    occupancy_rate = 0.8
    revenue = 20018.67
    profit_margin = 0.45