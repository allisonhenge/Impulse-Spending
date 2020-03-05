import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

from hotel_class import Hotel
import compare_data
name = 'The Make Believe Crowne'
input_brand = 'IHG - International Hotel Group'
input_flag = 'Crowne Plaza'
input_rooms = 303
input_specialty_type = 'None'
input_occupancy_rate = 0.6
input_revenue = 20018.67
revenue_period = 'Quarterly'
input_profit = 0.25
profit_type = 'Profit Margin'
profit_period = 'Monthly'

cust_array = [name, input_brand, input_flag, input_rooms, input_specialty_type, \
input_occupancy_rate, input_revenue, revenue_period, input_profit, profit_type, profit_period]

def create_customer_results(customer_array):
    classified_hotel = Hotel(customer_array)
    customer_inputs = compare_data.create_hotel_variables(classified_hotel)
    comparison_df = compare_data.get_comparison_df(customer_inputs)
    create_results = compare_data.compare_data(comparison_df, customer_inputs)
    return create_results
results = create_customer_results(cust_array)
print(results)

if __name__ == "__main__":
    pass


