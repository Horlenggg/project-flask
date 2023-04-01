
from Views import view
from flask import request,jsonify
from Model import MyModel
class StudentController:
    

    def __init__(self) -> None:
        pass

    
    def addStudent():
        student = request.form
        if student['name'] and student['email'] and student['phone']:
            return MyModel.saveStudent(student)
        else :
            return jsonify(dict(student=student))

    def delete(id:str):
        if id is not None:
            return MyModel.delete_student(id)
        else :
            return jsonify({'ms':'System error...!'})
        
    def upadteStudent(id:str):
        try:
            if len(id) == 24:
                student = request.form
                if student['name'] and student['email'] and student['phone']:
                    return MyModel.update_student(id, student['name'], student['email'], student['phone'])
                else :
                    return jsonify({'ms':'all field are required'})
            else :
                return jsonify({'ms':'System error...!'})
        except:
            return jsonify({'ms':'System error...!'})
        
    
        