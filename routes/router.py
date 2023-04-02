from flask import Blueprint,session
from datetime import datetime,timedelta
from Controller import AuthController,MyController
import jwt

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

@router.get('/create-session')
def create_session():
    session['abc'] = 'Hello, world'
    return dict({'ms':'message created'})

@router.get('/get-session')
def get_session():
    if 'abck' in session:
        abc =session['abck']
        return abc
    return 'authentications'

@router.get('/create-token/<data>')
def create_token(data):
    token = jwt.encode({
        'password':data,
        'exp':datetime.utcnow() + timedelta(minutes=5)
    },"dkkmeveuuveuuve")
    return dict(token=token)    


# @router.get('signUp')
# def signUp():
#     return AuthController.