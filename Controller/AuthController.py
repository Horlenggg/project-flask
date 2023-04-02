from flask import request,redirect
from Views import view
from applications import *
from Model import MyModel
class AuthController:
    pass

    def Login():
        return view.renderThemplate(DIRECTORY_PAGE_AUTH,LOGIN_PAGE,FILE_TEXT_VIEWS)
    

    def requestLogin():
        data = request.form
        if data['email'] and data['password']:
            return MyModel.requestLogin(data['email'],data['password'])
        else :
            return "All field are required" 
    
    # def SignUp():
    #     return view.renderThemplate(DIRECTORY_PAGE)

