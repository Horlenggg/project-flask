from flask import Flask,render_template
from routes import router
app = Flask(__name__)


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