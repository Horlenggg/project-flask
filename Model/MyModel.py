from .AuthModel import AuthModel
from .db import db
from flask import redirect,Response,jsonify
from bson import json_util,ObjectId
from Views import view
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
        except:
            return jsonify({"message":"somethong wrong"})
    def requestLogin(email,password):
        try:
            users = db['users'].find_one({'email': email,'password': password})
            # return Response(json_util.dumps(users),mimetype='application/json')
            if users:
                return redirect('/home')
            else :
                return jsonify({"message":"Unauthentications"})
        except:
                return jsonify({"message":"Unauthentications"})

        
    def saveStudent(data):
        id = db['student'].insert_one({'name':data['name'],'email':data['email'],'phone':data['phone']})
        print(str(id))
        return redirect('/home')
    
    def delete_student(id:str):
        try:
            delete_id = db['student'].delete_one({'_id':ObjectId(id)})
            if str(delete_id):
                return redirect('/home')
            else :
                return jsonify({'ms':'something wrong'})
        except:
                return jsonify({'ms':'something wrong'})


    def update_student(id:str,name:str,email:str,phone:str):
        try:
            query = {'name':name,'email':email,'phone':phone}
            student = db['student'].update_one({'_id':ObjectId(id)},{'$set':query})
            if student:
                return redirect('/home')
            else :
                return jsonify({'ms':'something wrong'})
        except:
            return jsonify({'ms':'something wrong'})
        
    def get_student_data(id:str):
        try:
            student = db['student'].find_one({'_id':ObjectId(id)})
            if student is not None:
                return view.renderUpdatePage(dict(student))
            else :
                return jsonify({'ms':'something wrong'})
        except :
            return jsonify({'ms':'something wrong'})