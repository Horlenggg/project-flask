from flask import Flask,render_template,session
from routes import router
from flask_session import  Session
app = Flask(__name__)

# app.config["SESSION_PERMANENT"] = False
app.secret_key="horleng"
SESSION_TYPE = "filesystem"
app.config.from_object(__name__)
Session(app)

app.register_blueprint(router)



@app.errorhandler(404)
def pageNotfound(error):
    return render_template("page/Defualt.html"),404


@app.get('/')
def greeting():
    return {"ms":"Hello dear, Wellcome to my website...!"}



if __name__ == '__main__':
    app.run(
        host="localhost",
        port=5000,
        debug=True
    )