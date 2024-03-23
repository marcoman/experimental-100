from flask import Flask
from flask import render_template
import requests

JSON_ENDPOINT = "https://api.npoint.io/0c76fe97addb8a7e70ed"

app = Flask(__name__)

# Read json file
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
response=requests.get(JSON_ENDPOINT, headers=headers)
blog_json = response.json()
print (blog_json)

@app.route('/')
def hello():
    return render_template('index.html', blog=blog_json)

@app.route('/index.html')
def index():
    return render_template('index.html', blog=blog_json)

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:index>')
def post(index):
    request_post = None
    for blog in blog_json:
        if blog["id"] == index:
            request_post = blog
    return render_template('post.html', post=request_post)

if __name__ == "__main__":
    app.run(debug=True)

