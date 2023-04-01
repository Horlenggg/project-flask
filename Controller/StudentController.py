
from Views import view
from applications import *

class StudentController:
    

    def __init__(self) -> None:
        pass

    def Home():
        return view.renderThemplate(DIRECTORY_PAGE,HOME_PAGE,FILE_TEXT_VIEWS)