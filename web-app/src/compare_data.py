import numpy as np
import pandas as pd

from pandas import ExcelWriter
from pandas import ExcelFile

flag_groupings = pd.read_excel('../../data/flag-groupings.xlsx')
clean_sales_data = pd.read_csv('../data/clean_sales_data.csv')

def get_comparison_df(brand, flag, size_subset, hotel_type, hotel_group):
    if brand == 'Not Hotel':
        comparison_df = 'Not Hotel Data'
    elif brand == 'Hilto':
        brand_mask = clean_sales_data['Brand'] == 'Hilto'
        brand_df = clean_sales_data[brand_mask].copy()
        flag_mask = brand_df['Flag'] == flag
        size_mask = brand_df['Size Subset'] == size_subset
        flag_df = brand_df[flag_mask & size_mask].copy()
        if len(flag_df) > 0:
            hilton_comparison_df = flag_df.copy()
        elif len(flag_df) <= 24:
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
        if len(flag_df) > 24:
            IHG_comparison_df = flag_df.copy()
        elif len(flag_df) <= 24:
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





if __name__ == "__main__":
    pass