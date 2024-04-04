from aiohttp import request
from flask import app, render_template
from psutil import users
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and (users[username], password):
            return render_template('secured_page.html', username=username)
        else:
            return render_template('error.html', error_message='Invalid username or password!')
    return render_template('login.html')
