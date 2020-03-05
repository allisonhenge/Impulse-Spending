import numpy as np
import pandas as pd

from pandas import ExcelWriter
from pandas import ExcelFile
import json

flag_groupings = pd.read_excel('../../../data/flag-groupings.xlsx')
clean_sales_data = pd.read_csv('../../data/clean-sales-data.csv')

def create_hotel_variables(classified_hotel):
    name = classified_hotel.name
    brand = classified_hotel.brand
    flag = classified_hotel.flag
    num_rooms = classified_hotel.num_rooms
    room_range = classified_hotel.room_range
    size_subset = classified_hotel.size_subset
    hotel_type = classified_hotel.hotel_type
    hotel_group = classified_hotel.hotel_group
    specialty_type = classified_hotel.specialty_type
    occupancy_rate = classified_hotel.occupancy_rate
    current_revenue = classified_hotel.current_revenue
    current_profit = classified_hotel.current_profit
    current_profit_margin = classified_hotel.current_profit_margin
    current_SPOR = classified_hotel.current_SPOR
    customer_inputs = [name, brand, flag, num_rooms, room_range, size_subset, hotel_type, hotel_group, specialty_type, \
                        occupancy_rate, current_revenue, current_profit, current_profit_margin, current_SPOR] 
    return customer_inputs    


def get_comparison_df(customer_inputs):
    name, brand, flag, num_rooms, room_range, size_subset, hotel_type, hotel_group, specialty_type, \
    occupancy_rate, current_revenue, current_profit, current_profit_margin, current_SPOR = customer_inputs
    
    big_brands = ['Hilto', 'IHG']
    if brand == 'Not Hotel':
        comparison_df = 'Not Hotel Data'
    elif brand in big_brands:
        brand_mask = clean_sales_data['Brand'] == brand
        brand_df = clean_sales_data[brand_mask].copy()
        flag_mask = brand_df['Flag'] == flag
        size_mask = brand_df['Size Subset'] == size_subset
        flag_df = brand_df[flag_mask & size_mask].copy()
        if len(flag_df) > 0:
            brand_comparison_df = flag_df.copy()
        elif len(flag_df) <= 24:
            type_mask = brand_df['Type'] == hotel_type
            group_mask = brand_df['Group'] == hotel_group
            brand_comparison_df = brand_df[type_mask & group_mask & size_mask].copy()
        comparison_df = brand_comparison_df.copy()
    else:
        type_mask = clean_sales_data['Type'] == hotel_type
        group_mask = clean_sales_data['Group'] == hotel_group
        size_mask = clean_sales_data['Size Subset'] == size_subset
        other_brands_comparison_df = clean_sales_data[type_mask & group_mask & size_mask].copy()
        comparison_df = other_brands_comparison_df
    return comparison_df

def compare_data(comparison_df, customer_inputs):
    name, brand, flag, num_rooms, room_range, size_subset, hotel_type, hotel_group, specialty_type, \
    occupancy_rate, current_revenue, current_profit, current_profit_margin, current_SPOR = customer_inputs

    if type(comparison_df) == str or current_revenue == 'No Current Retail Revenue' or \
        current_profit_margin == 'Not Currently Profitable' or \
        hotel_group == 'Not Hotel' or hotel_type == 'Not Hotel' or \
        specialty_type != 'None':
        results = "Our robot could not compare your data to enough similar hotels to be accurate. \
        That just means we get to contact you directly through the email you've provided"
    else:
        est_SPOR = comparison_df['SPOR'].mean()
        change_SPOR = est_SPOR - current_SPOR
        est_revenue = est_SPOR * (num_rooms*30.62*occupancy_rate)
        change_revenue = est_revenue - current_revenue
        cost = current_revenue - current_profit
        est_profit = est_revenue - cost
        est_profit_margin = est_profit/est_revenue
        change_profit_margin = est_profit_margin - current_profit_margin
        if change_SPOR <= 0:
            results = "Our robot could not compare your data to enough similar hotels to be accurate. \
            That just means we get to contact you directly through the email you've provided"
        else:
            results = [name, current_SPOR, est_SPOR, change_SPOR, current_revenue, est_revenue, \
                        change_revenue, current_profit_margin, est_profit_margin, change_profit_margin]
        # with open('saved_results.json', 'w') as filehandle:
        #     json.dump(results, filehandle)
    return results

if __name__ == "__main__":
    # name = 'The Make Believe Crowne'
    # input_brand = 'IHG - International Hotel Group'
    # input_flag = 'Crowne Plaza'
    # input_rooms = 303
    # input_specialty_type = 'None'
    # input_occupancy_rate = 0.6
    # input_revenue = 20018.67
    # revenue_period = 'Quarterly'
    # input_profit = 0.45
    # profit_type = 'Profit Margin'
    # profit_period = 'Monthly'
    
    # cust_array = [name, input_brand, input_flag, input_rooms, input_specialty_type, input_occupancy_rate, input_revenue, revenue_period, input_profit, profit_type, profit_period]

    # classified_hotel = Hotel(cust_array)
    pass