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


# @router.get('signUp')
# def signUp():
#     return AuthController.