from .AuthModel import AuthModel
from .db import db
from flask import redirect,Response,jsonify,session
from bson import json_util,ObjectId
from Views import view
from werkzeug.security import generate_password_hash,check_password_hash
import jwt
from datetime import datetime,timedelta
import os

class MyModel(AuthModel):

    def __init__(self):
         super().__init__(self)

    def getStudent():
        try:
            students = db['student'].find().sort('name')
            # students = json_util.dumps(students)
            # print(students)
            students = enumerate(students,start=1)
            return view.renderHomePage(students)
        except Exception as e:
                return jsonify({"message":str(e)})
    def requestLogin(email,password):
        try:
            users = db['users'].find_one({'email': email,'password': password})
            if users:
                data = {'email':email,'password':password}
                token = jwt.encode({
                    'data':data,
                    'exp': datetime.utcnow() + timedelta(hours=24)
                },os.getenv("SECRET_KEY"),algorithm="HS256")
                session['token'] = token
                return redirect('/')
            else :
                return jsonify({"message":"Unauthentications"})
        except Exception as e:
                return jsonify({"message":str(e)})

        
    def saveStudent(data):
        id = db['student'].insert_one({'name':data['name'],'email':data['email'],'phone':data['phone']})
        print(str(id))
        return redirect('/')
    
    def delete_student(id:str):
        try:
            delete_id = db['student'].delete_one({'_id':ObjectId(id)})
            if str(delete_id):
                return redirect('/')
            else :
                return jsonify({'ms':'something wrong'})
        except Exception as e:
                return jsonify({"message":str(e)})


    def update_student(id:str,name:str,email:str,phone:str):
        try:
            query = {'name':name,'email':email,'phone':phone}
            student = db['student'].update_one({'_id':ObjectId(id)},{'$set':query})
            if student:
                return redirect('/')
            else :
                return jsonify({'ms':'something wrong'})
        except Exception as e:
                return jsonify({"message":str(e)})
        
    def get_student_data(id:str):
        try:
            student = db['student'].find_one({'_id':ObjectId(id)})
            if student is not None:
                return view.renderUpdatePage(dict(student))
            else :
                return jsonify({'ms':'something wrong'})
        except Exception as e:
                return jsonify({"message":str(e)})