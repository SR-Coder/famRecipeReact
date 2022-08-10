from flask import Flask, request, render_template, redirect, session, flash
from flask_jwt_extended import create_access_token, get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager
from flask_bcrypt import Bcrypt
from flask_app.config.config import Config
from flask_cors import CORS, cross_origin
import re

app = Flask(__name__)
cors = CORS(app)

api = app
db = Config.DATABASE_NAME
bcrypt = Bcrypt()
app.config.from_object(Config)

jwt = JWTManager(api)