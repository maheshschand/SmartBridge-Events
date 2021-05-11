# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 13:30:13 2021

@author: rmahe
"""

from flask import Flask, request, render_template, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
app = Flask(__name__)
mysql = MySQL(app)

app.secret_key = 'a'
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "details"


@app.route('/')
def home():
    return render_template('apply.html')

@app.route('/uploaddata', methods=["POST"])
def uploaddata():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        stream = request.form["stream"]
        address = request.form["address"]
        
        session['name'] = name
        
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO newtable VALUES(NULL, % s, % s, % s, % s)', (name, email, stream, address))
        mysql.connection.commit()
        msg = "You have successfully got registered"
    return render_template("apply.html", msg = msg)

@app.route('/display')
def display():
    print(session['name'])
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM newtable WHERE name = % s', (session['name'],))
    mysql.connection.commit()
    account = cursor.fetchone()
    print(account)
    session.pop('name')
    return render_template("apply.html", account = account)
        
if __name__ == '__main__':
    app.run(debug = True)