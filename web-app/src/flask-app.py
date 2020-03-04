from flask import Flask, render_template, url_for, request, jsonify

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from src.input_fields import create_cust_options
from src.hotel_class import Hotel
flag_groupings = pd.read_excel('../../data/flag-groupings.xlsx')

app = Flask(__name__)
app.debug = True
#when submit button hit on front end, run hotel_classifier.py

@app.route('/', methods=['GET'])
#read in json to output to React or html

if __name__ == "__main__":
    flag_groupings_filepath='../../data/flag_groupings.xlsx'
    app.run(host = '0.0.0.0', port='8000', debug=True)