#pip install flask
import random as r
from flask import Flask,render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/ljubezn",methods=["POST"])
def love_calc():
    #print(request.form)
    i1=request.form["ime1"]
    i2=request.form["ime2"]
    if i1.lower()==i2.lower():
        pr=100
        komentar="Samoljubje"
    elif i1.strip().lower()=="žan" or i2.strip().lower()=="žan":
        pr=r.randint(90,100)
        if "x" in i1 or "x" in i2:
            pr*=2
            if pr>100:
                pr=100
    elif i1.strip().lower()=="david" or i2.strip().lower()=="david":
        pr=r.randint(0,10)
        if "x" in i1 or "x" in i2:
            pr*=2
            if pr>100:
                pr=100
    else:
        pr=r.randint(0,100)
        if "x" in i1 or "x" in i2:
            pr*=2
            if pr>100:
                pr=100
    if komentar!="Samoljubje":
        if pr < 30:
            komentar = "Pozabi"
        elif pr < 70:
            komentar = "Morda"
        else:
            komentar = "Poroka!" 
    return render_template("index.html",ime1=i1,ime2=i2,p=pr,iz=komentar)

app.run(debug=True)