from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SelectField

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET'])
def dropdown():
    brands = ['Best Western International', 'Choice International', 'IHG', 'Hilton Worldwide', 'Marriott International', 'Wyndham Hotel Group', 'Independant', 'Other']
    return render_template('test.html', brands=brands)

if __name__ == "__main__":
    app.run()