from .AuthModel import AuthModel
from .db import db
from flask import redirect,Response,jsonify
from bson import json_util
class MyModel(AuthModel):

    def __init__(self):
         super().__init__(self)


    def requestLogin(email,password):
        users = db['users'].find_one({'email': email,'password': password})
        # return Response(json_util.dumps(users),mimetype='application/json')
        if users:
            return redirect('/home')
        else :
            return jsonify({"message":"Unauthentications"})

         