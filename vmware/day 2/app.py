# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 13:30:13 2021

@author: rmahe
"""

from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('apply.html')

@pp.route('/uploaddata', method=["POST"])
def uploaddata():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        stream = request.form["stream"]
        address = request.form["address"]
        a = [name, email, stream, address]
    return render_template("apply.html", msg = a)
if __name__ == '__main__':
    app.run(debug = True)