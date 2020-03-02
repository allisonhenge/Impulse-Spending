from flask import Flask, render_template, url_for, request, jsonify

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from src.input_fields import create_cust_options
from src.hotel_class import Hotel
flag_groupings = pd.read_excel('../../data/flag-groupings.xlsx')

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET'])
def cust_inputs(brand_and_flags, specialty_service, revenue_period, profit_type):
    return create_cust_options(brand_and_flags, specialty_service, revenue_period, profit_type)

#read in json

@app.route('/', methods=['GET'])


#input class_hotel to comparison.py

# comparison.py output to flask
# flask to react

if __name__ == "__main__":
    flag_groupings_filepath='../../data/flag_groupings.xlsx'
    app.run(host = '0.0.0.0', port='8000', debug=True)