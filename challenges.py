from flask import Flask, request, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Required

import requests
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.debug = True

@app.route('/')
def home():
    return "Hello, world!"
    
class itunesForm(FlaskForm):
    artist = StringField('Enter Artist', validators=[Required()])
    api = IntegerField('Enter the number of results?', validators=[Required()])
    email = IntegerField('Enter your email', validators=[Required(), Email()])
    submit = SubmitField('Submit')

@app.route('/itunes-form')
def itunes_form():
    simpleForm = itunesForm()
    return render_template('itunes-form.html', form=simpleForm) # HINT : create itunes-form.html to represent the form defined in your class

@app.route('/itunes-result', methods = ['GET', 'POST'])
def itunes_result():
    form = itunesForm(request.form)
    if method == "POST" and form.validate_on_submit():
        artist = form.artist.data
        api = form.api.data
        params = {}
        params['term'] = artist
        params['limit'] = api
        response = requests.get('https://itunes.apple.com/search', params = params)
        response_py = json.loads(response.text)
    flash('All fields are required!')
    return render_template('itunes-result.html', result_html = response_py)

if __name__ == '__main__':
    app.run()
