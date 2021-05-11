# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 13:18:35 2021

@author: rmahe
"""

from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)
app.secret_key = 'a'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'jobportal'
mysql = MySQL(app)

@app.route('/')
def homer():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)