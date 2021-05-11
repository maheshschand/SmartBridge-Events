# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 12:21:11 2021

@author: rmahe
"""

from flask import Flask, redirect, url_for
app = Flask(__name__)
# @app.route('/hello/<name>') # app.route(rule, options)
# def hello_world(name):
#     return "hello %s" %name
# @app.route('/hello1/<int:value>') # app.route(rule, options)
# def hello1(name):
#     return "hello %d" %value
# @app.route('/user/<user>')
# def user(user):
#     return "Hello user %s" %user
# @app.route('/')
# def home():
#     return "this is home page but changes"

@app.route('/admin')
def hello_admin():
    return "hello admin"

@app.route('/guest/<guest>')
def hello_guest(guest):
    return "hello %s guest" %guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for('hello_guest', guest = name))
if __name__ == '__main__':
    app.run(debug = True) # local host web browser