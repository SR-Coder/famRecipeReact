from functools import wraps

from flask import redirect
from flask_app import session

# helper function so that you can check to see if someone is logged in before running the function
# simply a decorator function that passes wraps the routeing logic and either returns the function
# or redirects back to the login page

def is_loggedIn(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect('/')
        else:
            return func(*args, **kwargs)
    return wrapper