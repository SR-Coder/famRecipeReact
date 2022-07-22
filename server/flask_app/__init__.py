from flask import Flask, request, render_template, redirect, session, flash
from flask_jwt_extended import create_access_token, get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager
from flask_bcrypt import Bcrypt
import re

db = 'react_family_recipe_schema'

bcrypt = Bcrypt()

app = Flask(__name__)