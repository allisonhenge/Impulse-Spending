import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

from hotel_class import Hotel
from compare_data import create_hotel_variables, compare_data
# from compare_data import get_comparison_results

# read in customer hotel inputs
customer_array = pd.read_json('customer-inputs.json')

#apply Hotel class to customer input
classified_hotel = Hotel(customer_array)

#run through comparison file
# results = compare_data()

#save results to json to read into flask
# results.save_to_json('results.json')




