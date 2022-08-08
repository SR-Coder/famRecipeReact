# A User object to manage who is logged in.  really only for admins

from flask_app import app, db, session, bcrypt, re, flash
from flask_app.config.mysqlconnections import connectToMySQL
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data) -> None:
        self.id = data["id"]
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data["email"]
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s );"

        plain_pass = data['password']
        pw_hash = bcrypt.generate_password_hash(plain_pass)

        data = {
            **data,
            "password":pw_hash
        }

        user_id = connectToMySQL(db).query_db(query, data)
        return user_id
    @classmethod
    def CREATE_ADMIN(cls):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s );"

        plain_pass = 'asdfasdf'
        pw_hash = bcrypt.generate_password_hash(plain_pass)

        data = {
            "first_name":"James",
            "last_name":"Reeder",
            "email":"reederje@gmail.com",
            "password":pw_hash
        }

        user_id = connectToMySQL(db).query_db(query, data)
        return user_id


    @classmethod
    def get_one_user(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(db).query_db(query, data)
        if len(results)<1:
            return False
        return cls(results[0])

    @classmethod
    def update_user(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, password=%(password)s, updated_at=NOW() WHERE id=%(id)s;"
        results = connectToMySQL(db).query_db(query,data)
        return results

    @classmethod
    def login_user(cls, data):
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid Email/Password", "login")
            return False
        
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(db).query_db(query, data)

        if len(results) < 1:
            flash("Invalid Email/Password", "login")
            return False
        
        user_in_db = cls(results[0])
        if not bcrypt.check_password_hash(user_in_db.password, data['password']):
            flash("Invalid Email/Password", "Login")
            return False

        session["user_id"] = user_in_db.id
        return True

    @classmethod
    def token_user_login(cls,data):
        if not EMAIL_REGEX.match(data['email']):
            msg = {
                "error": "Not a valid email address/password!",
                "status": False
            }
            return msg

        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(db).query_db(query, data)

        if len(results) < 1:
            msg = {
                "error": "Not a valid email address/password!",
                "status": False
            }
            return msg

        user_in_db = cls(results[0])
        if not bcrypt.check_password_hash(user_in_db.password, data['password']):
            msg = {
                "error": "Not a valid email address/password!",
                "status": False
            }
            return msg

        return {"status":True}

    

    @staticmethod
    def validate_user(data):
        is_valid = True
        if len(data['first_name']) < 3:
            is_valid = False
            flash("First name must be longer than 3 characters", "register")

        if len(data['last_name']) < 3:
            is_valid = False
            flash("Last name must be longer than 3 characters", "register")

        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!", "register")
            is_valid = False

        if User.get_one_user(data):
            flash("this email is already in use!", 'register')
            is_valid = False

        if len(data['password']) < 7:
            is_valid = False
            flash("Password must be longer than 8 characters", "register")

        if data['cpass'] != data['password']:
            is_valid = False
            flash("Passwords must match!", "register")

        return is_valid