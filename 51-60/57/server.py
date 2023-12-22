from datetime import datetime
from random import randint
from flask import Flask, render_template
from flask import render_template

import requests

URL_AGEIFY="https://api.agify.io/?name="
URL_GENDERIZE="https://api.genderize.io/?name="
URL_SAMPLE_BLOG="https://api.npoint.io/c790b4d5cab58020d391"

app = Flask(__name__)

@app.route('/')
def hello_world():
    randnum = randint(1,100)
    current_year = datetime.now().year
    return render_template('index.html', 
                           randnum=randnum,
                           current_year=current_year,
                           )


@app.route('/guess/<name>')
def guess(name):
    response_age = requests.get(URL_AGEIFY + name)
    response_gender = requests.get(URL_GENDERIZE + name)
    age = response_age.json()['age']
    gender = response_gender.json()['gender']

    return render_template('guess.html', 
                           name=name,
                           gender=gender,
                           age=age)


@app.route('/blog/<num>')
def blog(num):
    print(num)
    response = requests.get(URL_SAMPLE_BLOG)
    all_posts = response.json()
    return render_template('blog.html', 
                           posts=all_posts)

# Run the app if we're running standalone
if __name__ == "__main__":
    app.run(debug=True)

