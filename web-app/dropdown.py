from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SelectField
from pandas import ExcelWriter
from pandas import ExcelFile

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET'])
def dropdown():
    flag_groupings = pd.read_excel(flag_groupings_filepath)
    unique_brands = list(flag_groupings['Brand'].unique()) + ['Other', 'Retail', 'Apartment']
    def get_brand_flags(brand):
        brand_flags_mask = flag_groupings['Brand'] == brand
        brand_df = flag_groupings[brand_flags_mask]
        brand_unique_flags = list(brand_df['Flag'].unique()) + ['Other']
        return brand_unique_flags

    brand_and_flags = {}
    for brand in unique_brands:
        brand_and_flags[brand] = get_brand_flags(brand)

    

    return render_template('test.html', brands=unique_brands)

if __name__ == "__main__":
    flag_groupings_filepath='../data/flag_groupings.xlsx'
    app.run()