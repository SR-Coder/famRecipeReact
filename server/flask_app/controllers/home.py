from operator import imod
import re

from flask import redirect, session
from flask_app import app, render_template, request
from flask_app.helpers.helper import is_loggedIn
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template("landing_page.html")

@app.route('/createAdmin')
def create_me():
    User.CREATE_ADMIN()
    return redirect('/')

@app.post("/login")
def login():
    print(request.form)
    result = User.login_user(request.form)
    if not result:
        return redirect('/')
    return redirect('/api/how-to')



@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')