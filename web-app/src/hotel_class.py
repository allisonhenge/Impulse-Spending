import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib
import matplotlib.pyplot as plt


class Hotel(object):

    def __init__(self, cust_array):
        name, input_brand, input_flag, input_rooms, input_specialty_service, input_occupancy_rate, input_revenue, revenue_period, input_profit, profit_type, profit_period = cust_array
        self.flag_groupings = pd.read_excel('../../../data/flag-groupings.xlsx')
        self.name = name
        self.brand = input_brand
        self.flag = input_flag
        self.num_rooms = input_rooms
        self.specialty_service = input_specialty_service
        self.occupancy_rate = input_occupancy_rate
        self.revenue = input_revenue
        self.revenue_period = revenue_period
        self.profit = input_profit
        self.profit_type = profit_type
        self.profit_period = profit_period

    def get_brand(self):
        brand = ''
        if self.brand == 'Apartment':
            brand == 'Not Hotel'
        elif self.brand == 'Retail':
            brand = 'Not Hotel'
        elif self.brand == 'Hilton':
            brand =='Hilto'
        elif self.brand == 'IHG - International Hotel Group':
            brand =='IHG'
        else:
            brand='Other'
        return brand
    
    def get_room_range(self):
        rooms_plus_ten = int(input_rooms + input_rooms*0.1)
        rooms_minus_ten = int(input_rooms - input_rooms*0.1)
        room_range = [rooms_minus_ten, rooms_plus_ten]
        return room_range

    

    def get_size_subset(self):
        if self.num_rooms <= 0:
            size_subset = 0 
        elif 0 < self.num_rooms < 80:
            size_subset = 1
        elif 80 <= self.num_rooms < 100:
            size_subset = 2
        elif 100 <= self.num_rooms < 150:
            size_subset = 3
        elif 150 <= self.num_rooms < 200:
            size_subset = 4
        else:
            size_subset = 5
        return size_subset 
    
    def hotel_type(self):
        flag_mask = flag_groupings['Flag'] == input_flag
        if input_brand in ['Other', 'Retail', 'Apartment']:
            hotel_type = 'Not Hotel'
        else:
            type_df = flag_groupings[flag_mask]
            hotel_type = type_df['Type']
        return hotel_type
    
    def get_group(self):
        flag_mask = flag_groupings['Flag'] == self.flag
        if input_brand in ['Other', 'Retail', 'Apartment']:
            hotel_group = 'Not Hotel'
        else:
            group_df = flag_groupings[flag_mask]
            hotel_group = group_df['Group']
        return hotel_group
        
    def is_specialty(self):
        if input_specialty_service == 'None':
            specialty_service = 'None'
        else:
            specialty_service = input_specialty_service
        return specialty_service

    def get_occupancy_rate(self):
        if input_occupancy_rate == None:
            occupancy_rate = 0.68
        else:
            occupancy_rate = input_occupancy_rate
        return occupancy_rate

    def get_monthly_revenue(self):
        if input_revenue == 0:
            revenue = 'No Current Retail Revenue'
        elif revenue_period == 'Yearly':
            revenue = input_revenue/12
        elif revenue_period == 'Quarterly':
            revenue = input_revenue/4
        else:
            revenue = input_revenue
        return revenue

    def get_profit_margin(self):
        if input_profit == None or input_revenue == None:
            profit_margin = 'Not Currently Profitable'
        elif profit_type == 'Current Gross Profit':
            if profit_period == 'Yearly':
                profit_margin = (input_profit/12)/self.revenue
            elif profit_period == 'Quarterly':
                profit_margin = (input_profit/4)/self.revenue
            else:
                profit_margin = input_profit/self.revenue
        elif profit_type == 'Profit Margin':
            profit_margin = input_profit
        return profit_margin



if __name__ == "__main__":
    name = 'The Make Believe Crowne'
    input_brand = 'IHG'
    input_flag = 'Crowne Plaza'
    input_rooms = 303
    input_specialty_service = 'None'
    input_occupancy_rate = 0.8
    input_revenue = 20018.67
    revenue_period = 'Monthly'
    input_profit = 0.45
    profit_type = 'Profit Margin'
    profit_period = 'Monthly'
    

    