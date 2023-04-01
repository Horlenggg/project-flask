from flask import Blueprint
from Controller import AuthController,MyController

router = Blueprint('router',__name__)


@router.get('/home')
def home():
    return MyController.Home()

@router.post('/requestLogin')
def requestLogin():
    return AuthController.requestLogin()

@router.get('/login')
def Login():
    return AuthController.Login()

@router.post('/save-student')
def saveStudent():
    return MyController.addStudent()

@router.get('/delete/<id>')
def deleteStudent(id):
    return MyController.delete(id)

@router.get('/edite/<id>')
def editStudent(id):
    return MyController.update_stu_form(id)

@router.post('/get_update_student/<id>')
def get_update_student(id):
    return MyController.upadteStudent(id)


# @router.get('signUp')
# def signUp():
#     return AuthController.