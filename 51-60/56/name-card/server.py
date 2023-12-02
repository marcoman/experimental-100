from flask import Flask, render_template
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')


# Run the app if we're running standalone
if __name__ == "__main__":
    app.run(debug=True)

