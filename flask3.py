#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 14:14:22 2022

http://127.0.0.1:5000/hello 

https://www.tutorialspoint.com/flask/flask_variable_rules.htm
https://pythonspot.com/flask-web-app-with-python/

@author: andy
"""


from flask import Flask
app = Flask(__name__)


@app.route('/hello')
def hello_world():
   return 'hello world'


"""
@app.route("/hello/<name>")
def hello_name(name):
   return 'Hello %s!' % name
"""

if __name__ == '__main__':
   app.run(debug = True)