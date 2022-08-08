from datetime import datetime, timedelta, timezone
import json
from urllib import response
from flask import jsonify
from flask_jwt_extended import get_jwt, jwt_required
from flask_app import api, jwt, bcrypt, get_jwt_identity, create_access_token, unset_jwt_cookies, request
from flask_app.models.user import User

@api.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now+timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            data = response.get_json()
            if type(data) is dict:
                data['access_token'] = access_token
                response.data = json.dumps(data)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response




# Login to the API
@api.post('/api/token')
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    post_data = {
        "email":email,
        "password":password
    }
    status = User.token_user_login(post_data)
    if not status['status']:
        return {"msg":"Wrong email or password"}, 401

    access_token = create_access_token(identity=email)
    response = {"access_token":access_token}
    return response

# Logout from the API
@api.post('/api/logout')
def api_logout():
    response = jsonify({"msg":"logout successful"})
    unset_jwt_cookies(response)
    return response


@api.route("/api/test")
@jwt_required()
def text():
    res_body = {
        "msg": "yay you did it!!!",
        "error": "None"
    }
    return res_body