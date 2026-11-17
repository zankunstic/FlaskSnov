#pip install flask

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/o-meni")
def about():
    return "moje ime je žan in to je to"

app.run(debug=True)