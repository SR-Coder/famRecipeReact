from flask_app import app, render_template

@app.route('/')
def index():
    return render_template("landing_page.html")

@app.post("/login")
def login():
    pass