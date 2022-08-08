from flask_app import app, render_template, redirect
from flask_app.helpers.helper import is_loggedIn




@app.route('/api/how-to')
@is_loggedIn
def how_to():
    return render_template('api.html')

