# Family recipe backend API
import imp
from flask_app import app
from flask_app.controllers import home


if __name__ == "__main__":
    app.run(debug=True, port=5000)

