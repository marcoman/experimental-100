# Imports
from PIL import Image

from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL, NumberRange

from flask import request
from flask import url_for
import os
import requests
import json

FREESOUND_API_KEY = os.environ.get("FREESOUND_API_KEY")
# The Curl command is of this form:
# curl "https://freesound.org/apiv2/search/text/?query=piano&token=YOUR_API_KEY"

URL_FREESOUND = "https://freesound.org"
FREESOUND_SEARCH = "apiv2/search/text"
FREESOUND_DOWNLOAD = "apiv2/sounds"

class QueryForm(FlaskForm):
    query = StringField('Query', validators=[DataRequired(), Length(min=1, max=100)]
                        , render_kw={"placeholder": "Enter your query here"})
    submit = SubmitField('Submit')

    
def query_freesound(queryvalue):
    print(f"Querying freesound with {queryvalue}")
    # Get the response via our requests library
    response = requests.get(f'{URL_FREESOUND}/{FREESOUND_SEARCH}', params={'query': queryvalue, 'token': FREESOUND_API_KEY})
    jbody = response.json()
    return jbody["results"]
    
def print_results(dict_test):
    for item in dict_test:
        print(f'The id is {item["id"]} name is {item["name"]}')

def get_id_from_name(name):
    for item in dict_test:
        if item["name"] == name:
            return item["id"]
    return None
    
def download_file(id, name):
    URL_FREESOUND_DOWNLOAD = f"{URL_FREESOUND}/{FREESOUND_DOWNLOAD}/{id}/download"
    response = requests.get(URL_FREESOUND_DOWNLOAD, params={'token': FREESOUND_API_KEY})
    with open(f"{name}", 'wb') as f:
        f.write(response.content)

def add_url(dict_test):
    for item in dict_test:
        print(f'Adding to {item["id"]} in this body {item} ')
        item["download"] = f"{URL_FREESOUND}/{FREESOUND_DOWNLOAD}/{item['id']}/download"
        print(f'Added {item["download"]}')

dict_test = query_freesound("piano")

app = Flask(__name__)
Bootstrap5(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


# all Flask routes below
@app.route("/", methods=['GET', 'POST'])
def home():
    # If the user pressed submit, then we have to load a new page.
    if request.method == 'POST':
        print("POST")
        sounds = request.form.get('data')
        query = request.form.get('query')
    else:
        query = "piano"
        sounds = query_freesound(query)
    add_url(sounds)
    return render_template('index.html', sounds=sounds, query=query)

# Do your query here
@app.route("/query", methods=["GET", "POST"])
def query():
    form = QueryForm()
    if form.validate_on_submit():
        query=form.query.data
        print(f"Query is {query}")
        dict_test = query_freesound(query)
        add_url(dict_test)
        # print(f"dict_test is {dict_test}")
        return render_template('index.html', sounds=dict_test, query=query)
    return render_template("query.html", form=form)
