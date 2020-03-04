import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib
import matplotlib.pyplot as plt


class Hotel(object):

    def __init__(self, cust_array):
        name, input_brand, input_flag, input_rooms, input_specialty_type, input_occupancy_rate, input_revenue, revenue_period, \
        input_profit, profit_type, profit_period = cust_array
        self.flag_groupings = pd.read_excel('../../../data/flag-groupings.xlsx')
        self.name = name
        self.brand = self.comparison_brand(input_brand)
        self.flag = input_flag
        self.num_rooms = input_rooms
        self.room_range = self.get_room_range()
        self.size_subset = self.get_size_subset()
        self.hotel_type = self.get_hotel_type(input_flag)
        self.hotel_group = self.get_hotel_group()#
        self.specialty_type = input_specialty_type
        self.occupancy_rate = self.get_occupancy_rate(input_occupancy_rate)
        self.current_revenue = self.get_monthly_revenue(input_revenue, revenue_period)
        self.current_profit = self.get_profit(input_revenue, input_profit, profit_type, profit_period)
        self.current_profit_margin = self.current_profit/self.current_revenue
        self.current_SPOR = self.get_SPOR()

    def comparison_brand(self, input_brand):
        if input_brand in ['Apartment', 'Retail']:
            self.brand = 'Not Hotel'
        elif input_brand == 'Hilton':
            self.brand = 'Hilto' #brands have a to 5 character limit in sales data
        elif input_brand == 'IHG - International Hotel Group':
            self.brand = 'IHG'
        else:
            self.brand = 'Other'
        return self.brand
    
    def get_room_range(self):
        rooms_plus_ten = int(self.num_rooms + self.num_rooms*0.1)
        rooms_minus_ten = int(self.num_rooms - self.num_rooms*0.1)
        self.room_range = [rooms_minus_ten, rooms_plus_ten]
        return self.room_range

    def get_size_subset(self):
        if self.num_rooms <= 0:
            self.size_subset = 0 
        elif self.num_rooms < 80:
            self.size_subset = 1
        elif self.num_rooms < 100:
            self.size_subset = 2
        elif self.num_rooms < 150:
            self.size_subset = 3
        elif self.num_rooms < 200:
            self.size_subset = 4
        else:
            self.size_subset = 5 
        return self.size_subset
    
    def get_hotel_type(self, input_flag):
        flag_mask = self.flag_groupings['Flag'] == input_flag
        if self.brand == 'Not Hotel':
            self.hotel_type = 'Not Hotel'
        else:
            type_df = self.flag_groupings[flag_mask]
            # self.hotel_type = str(list(type_df['Type']))
            self.hotel_type = type_df.iloc[0]['Type']
            return self.hotel_type
    
    def get_hotel_group(self):
        flag_mask = self.flag_groupings['Flag'] == self.flag
        if self.brand == 'Not Hotel':
            self.hotel_group = 'Not Hotel'
        else:
            group_df = self.flag_groupings[flag_mask]
            self.hotel_group = group_df.iloc[0]['Group']
        return self.hotel_group

    def get_occupancy_rate(self, input_occupancy_rate):
        if input_occupancy_rate == None:
            self.occupancy_rate = 0.68
        elif input_occupancy_rate > 1:
            self.occupancy_rate = input_occupancy_rate/100
        else:
            self.occupancy_rate = input_occupancy_rate
        return self.occupancy_rate

    def get_monthly_revenue(self, input_revenue, revenue_period):
        if input_revenue == 0 or input_revenue is None:
            self.current_revenue = 'No Current Retail Revenue'
        elif revenue_period == 'Yearly':
            self.current_revenue = input_revenue/12
        elif revenue_period == 'Quarterly':
            self.current_revenue = input_revenue/4
        else:
            self.current_revenue = input_revenue
        return self.current_revenue

    def get_profit(self, input_revenue, input_profit, profit_type, profit_period):
        if input_profit is None or input_revenue is None:
            self.current_profit = 'Not Currently Profitable'
        elif profit_type == 'Current Gross Profit':
            if profit_period == 'Yearly':
                self.current_profit = input_profit/12
            elif profit_period == 'Quarterly':
                self.current_profit = input_profit/4
            else:
                self.current_profit = input_profit
        elif profit_type == 'Profit Margin':
            self.current_profit = input_profit*self.current_revenue
        return self.current_profit

    def get_SPOR(self):
        self.current_SPOR = (self.current_revenue/(self.num_rooms*30.62*self.occupancy_rate))
        return self.current_SPOR


if __name__ == "__main__":
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

    classified_hotel = Hotel(cust_array)
    