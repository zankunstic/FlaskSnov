#pip install flask
import random as r
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/o-meni")
def about():
    return render_template("about.html")


# met kocke... random(1-6)
@app.route("/kocka")
def dice():
    return render_template("dice.html",kocka=r.randint(1,6))


@app.route("/kocka/<N>")
def dice2(N):
    return render_template("dice.html",kocka=r.randint(1,int(N)))




sezM=["Mark","David","Lovro","Kristjan"]
sezŽ=["Maja","Živa","Taja","Špela"]

@app.route("/prihodnost")
def future():
    ime1 = r.choice(sezM)
    ime2 = r.choice(sezŽ)
    procent = r.randint(0, 100)
    return render_template(   "future.html",
        ime1=ime1,
        ime2=ime2,
        procent=procent)

app.run(debug=True)