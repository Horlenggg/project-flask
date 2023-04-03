from .StudentController import StudentController
from applications import *
import jwt
import os
from Views import view
from Model import MyModel
from flask import jsonify,sessions,redirect,session

class MyController(StudentController):
    

    def __init__(self) -> None:
        super().__init__()

    def Home():
        try:
            if 'token' not in session:
                return redirect('/login')
            else :
                if session['token'] :
                    try:
                        token = session['token']
                        data = jwt.decode(token,os.getenv("SECRET_KEY"),algorithms="HS256")
                        if data is not None:
                            return MyModel.getStudent()
                        else :
                            return redirect('login')
                    except jwt.ExpiredSignatureError as err:
                        return redirect('login')
                else :
                    return redirect('login')
        except Exception as e:
            return dict(message = str(e))
    
    def update_stu_form(id):
        if len(id) == 24:
            return MyModel.get_student_data(id)
        else :
            return jsonify({'ms':'Invalid id'})