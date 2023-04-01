from flask import render_template
from applications import *

class view:

    def __init__(self) -> None:
        pass

    def renderThemplate(dir:str,filename:str,fileType):

        return render_template(dir+filename+fileType)
    def renderUpdatePage(student:dict):
        return render_template(DIRECTORY_PAGE+UPADTE_PAGE+FILE_TEXT_VIEWS,student=student,str=str)
    
    def renderHomePage(students:list):
        return render_template(DIRECTORY_PAGE+HOME_PAGE+FILE_TEXT_VIEWS,students = students,str=str)


