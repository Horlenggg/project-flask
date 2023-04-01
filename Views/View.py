from flask import render_template

class view:

    def __init__(self) -> None:
        pass

    def renderThemplate(dir:str,filename:str,fileType):
        return render_template(dir+filename+fileType)

