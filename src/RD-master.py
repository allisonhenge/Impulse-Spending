import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import openpyxl
pd.options.mode.chained_assignment = None

import matplotlib
import matplotlib.pyplot as plt
%matplotlib inline
plt.style.use("ggplot")

#read excel files for desired timeframe in pandas dataframes
sales_by_month = pd.read_excel(sales_filepath)
brand_and_flag = pd.read_excel(brand_and_flag_filepath)
flag_groupings = pd.read_excel(flag_groupings_filepath)



'''
reassign brands/flags add location type 
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

take all inputs and categorize hotel
calculate SPOR/ ROI? etc
auto generate message containing all hotel information plus calculations to impulsify
return SPOR and PM to customer on dashboard

'''

'''
robert - do you have actual occupancy rates for the hotels that are already customers?
did you generate or create the excel file for brand/flag
'''

if __name__ == "__main__":
    sales_filepath='../../capstone2/data/2019_sales_by_month.xlsx'
    brand_and_flag_filepath='../../capstone2/data/hotel_brand_and_flag.xlsx'
    #flag_groupings_filepath='../='