from .StudentController import StudentController
from applications import *
from Views import view
from Model import MyModel
from flask import jsonify,sessions,redirect

class MyController(StudentController):
    

    def __init__(self) -> None:
        super().__init__()

    def Home():
        return MyModel.getStudent()
        # if sessions['data']:
        # else :
        #     return redirect('/login')
    
    def update_stu_form(id):
        if len(id) == 24:
            return MyModel.get_student_data(id)
        else :
            return jsonify({'ms':'Invalid id'})