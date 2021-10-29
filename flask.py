# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 15:42:07 2021

@author: zidan
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()