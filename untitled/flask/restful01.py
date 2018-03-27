#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Time    : 2018/3/22 下午7:09
@Author  : ldx
@contact : ldx.9@163.com
@File    : restful01.py
@Software: PyCharm
'''

from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)
