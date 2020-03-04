from flask import Flask, render_template, url_for, request, jsonify

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import hotel_classifier

# from hotel_class import Hotel
flag_groupings = pd.read_excel('../../data/flag-groupings.xlsx')

app = Flask(__name__)
app.debug = True
#when brand dropdown selected return values in dictionary
@app.route('/')

@app.route('/get_brand', methods=['GET'])
react_input = readin_react_brand(react_brand)
input_brand = input_brand(react_input)

@app.route('/push_flags', method=['Post'])
unique_brands = list(flag_groupings['Brand'].unique()) + ['Other', 'Retail', 'Apartment']

def get_brand_flags(input_brand):
    brand_flags_mask = flag_groupings['Brand'] == input_brand
    brand_df = flag_groupings[brand_flags_mask]
    brand_unique_flags = list(brand_df['Flag'].unique()) + ['Other']
    return brand_unique_flags

brand_and_flags = {}
for brand in unique_brands:
    brand_and_flags[brand] = get_brand_flags(input_brand)

specialty_service = ['None', 'Airport', 'Convention Center']
revenue_period = ['Monthly', 'Quarterly', 'Yearly']
profit_type = ['Current Profit', 'Profit Margin']

create_cust_options = [brand_and_flags, specialty_service, revenue_period, profit_type]

with open('create_cust_options.json', 'w') as f:
    json.dump(create_cust_options, f)

#when submit button hit on front end, run hotel_classifier.py
@app.route('/run_classifier', method=['GET'])
readin_react_data = pd.read_json('saved_front_end.json')
create_results = hotel_classifier.create_customer_results(readin_react_data)

@app.route('/something_else', method=['GET'])
#read in json to output to React or html
readin_results = flask.read_json('saved_results.json')

if __name__ == "__main__":
    flag_groupings_filepath='../../data/flag_groupings.xlsx'
    app.run(host = '0.0.0.0', port='8000', debug=True)