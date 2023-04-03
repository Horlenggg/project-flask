from flask import Flask,render_template,session
from routes import router
from flask_session import  Session
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# app.config["SESSION_PERMANENT"] = False
app.config['SESSION_TYPE'] = "filesystem"
app.config['SECRET_KEY'] = 'vbrihvhrbsbveiiiiqekq'
app.config.from_object(__name__)
Session(app)

app.register_blueprint(router)



@app.errorhandler(404)
def pageNotfound(error):
    return render_template("page/Defualt.html"),404



if __name__ == '__main__':
    app.run(
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
        debug=True
    )