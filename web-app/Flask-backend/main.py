from flask import Flask, render_template, url_for, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
# import hotel_classifier
flag_groupings = pd.read_excel('../../data/flag-groupings.xlsx')

app = Flask("__name__")
app.debug = True


# class Form(FlaskForm):
#     brand = SelectField('Brand', choices=[('Hilton Worldwide', 'Hilton Worldwide'),
#                                             ('IHG - International Hotel Group', 'IHG - International Hotel Group'),
#                                             ('Marriott International / Starwood', 'Marriott International / Starwood'), 
#                                             ('Wyndham Hotels and Resorts', 'Wyndham Hotels and Resorts'),
#                                             ('Hyatt', 'Hyatt'),
#                                             ('Best Western', 'Best Western'),
#                                             ('Other', 'Other'),
#                                             ('Retail', 'Retail'),
#                                             ('Apartment', 'Apartment')], 
#                             validators=[DataRequired()])
#     flag = SelectField('Flag', choices = [], validators=[DataRequired()])
#     roomNumber = IntegerField('Number of Rooms', 
#                             validators=[DataRequired(), Length(min=1, max=5)])
#     specialType = SelectField('Specialty Type', choices=[('None', 'None'), 
#                                                 ('Airport', 'Airport'), 
#                                                 ('Convention Center', 'Convention Center')], 
#                             validators=[DataRequired()])
#     occupancyRate = IntegerField('Occupancy Rate in Percent', 
#                             validators=[DataRequired(), Length(min=1, max=5)])
#     revenue = IntegerField('Enter Revenue', 
#                             validators=[DataRequired(), Length(min=1, max=6)])
#     revenuePeriod = SelectField('Input Revenue Period', choices=[('Yearly', 'Yearly'), 
#                                                                 ('Quarterly', 'Quarterly'), 
#                                                                 ('Monthly', 'Monthly')], 
#                             validators=[DataRequired()])
#     profit = IntegerField('Enter Profit', 
#                             validators=[DataRequired(), Length(min=1, max=6)])
#     profitType = SelectField('Input Profit Type', choices=[('Current Profit', 'Current Profit'), 
#                                                                 ('Profit Margin', 'Profit Margin')], 
#                             validators=[DataRequired()])
#     profitPeriod = SelectField('Input Profit Period', choices=[('Yearly', 'Yearly'), 
#                                                                 ('Quarterly', 'Quarterly'), 
#                                                                 ('Monthly', 'Monthly')], 
#                             validators=[DataRequired()])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     submit = SubmitField('Submit')

@app.route('/React-frontend', methods=['GET', 'POST'])

def select_brand()
    form.brand.choices = [('Hilton', 'Hilton Worldwide'),
                            ('IHG', 'IHG - International Hotel Group'),
                            ('Marri', 'Marriott International / Starwood'), 
                            ('Wyndham', 'Wyndham Hotels and Resorts'),
                            ('Hyatt', 'Hyatt'),
                            ('Best Western', 'Best Western'),
                            ('Other', 'Other'),
                            ('Retail', 'Retail'),
                            ('Apartment', 'Apartment')]
    form.county.choices = [(row.ID, row.Name) for row in County.query.all()]
    if request.method == 'GET':
        return render_template('customerInput.js', form=form)
    if form.validate_on_submit() and request.form['form_name'] == 'PickCounty':
        # code to process form
        flash('state: %s, county: %s' % (form.state.data, form.county.data))
    return redirect(url_for('pick_county'))


@app.route   #('/', methods=['GET', 'Post'])
def route():
    if form1.validate_on_submit():
        form2.flag.choices = (k, v for key, value in brand_and_flags)
        return render_template("/", form1=form1, form2=form2)

    if form2.validate_on_submit():
        do.something()

    data=db.call()
    session.data = data
    form1 = HotelBrand()
    form2 = Flag()
    form1.choices = data.somefunction()
    form2.choices = ["",""]

    return render_template('/', form1=form1, form2=form2)

class BrandsAndFlags(brand_and_flags):




@app.route('/' methods=['GET', 'POST'])


if __name__ == "__main__":
    flag_groupings_filepath='../../data/flag_groupings.xlsx'
    app.run(host = '0.0.0.0', port='8000', debug=True)