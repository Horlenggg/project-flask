from flask import Blueprint,session
from datetime import datetime,timedelta
from Controller import AuthController,MyController
import jwt
import os

router = Blueprint('router',__name__)


@router.get('/')
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

@router.get('/logout')
def Logout():
    return AuthController.Logout()

@router.get('/create-session')
def create_session():
    session['abc'] = 'Hello, world'
    return dict({'ms':'message created'})

@router.get('/get-session')
def get_session():
    if 'abc' in session:
        abc =session['abc']
        return abc
    return 'authentications'

@router.get('/create-token')
def create_token():
    data = dict(username = "HelloWorld")
    try:
        token = jwt.encode({
            'password': data,
            'exp':datetime.utcnow() + timedelta(minutes=5)
            },os.getenv('SECRET_KEY'),algorithm="HS256")
        return dict(token=token)    
    except Exception as e:
        return dict(message = str(e))

@router.get('/decode-token/<token>')
def get_token(token ):
    print(token)
    try:
        data = jwt.decode(token,os.getenv("SECRET_KEY"),algorithms="HS256")
        return dict(data = data),200
    except Exception as e:
        return dict(meaage = str(e)),500


# @router.get('signUp')
# def signUp():
#     return AuthController.