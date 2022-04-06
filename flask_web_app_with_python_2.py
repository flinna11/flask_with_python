#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 13:51:40 2022

flask _web_app_with_python_2.py

https://www.tutorialspoint.com/flask/flask_variable_rules.htm
https://pythonspot.com/flask-web-app-with-python/
Open http://localhost:5000/ in your web browser, and “Hello World!” should appear.

http://127.0.0.1:5000/
http://127.0.0.1:5000/hello 
http://127.0.0.1:5000/members
http://127.0.0.1:5000/members/Jordan/


@author: andy
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Index!"


@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/members")
def members():
    return "Members"

"""
@app.route("/members/<string:name>/")
def getMember(name):
    return name</string:name>

"""

if __name__ == "__main__":
    app.run()
    
 