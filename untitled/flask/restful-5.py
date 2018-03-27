#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Time    : 2018/3/27 下午8:52
@Author  : ldx
@contact : ldx.9@163.com
@File    : restful-5.py
@Software: PyCharm
'''

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'
@app.route('/hello')
def hello():
    return 'Hello World'
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the giver id, the id is an integer
    return 'Post %d' % post_id

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
