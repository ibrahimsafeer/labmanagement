from flask import Flask, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_login import (
    login_required,
    logout_user,
    login_user,
    login_manager,
    LoginManager,
    current_user,
)


local_server = True
app = Flask(__name__)
app.secret_key = "TEMP"

login_manager = LoginManager(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return LabManagement.query.get(int(user_id))


app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/lab"
db = SQLAlchemy(app)


# class LabManagement(UserMixin,db.Model):


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


# @app.route('/admin' , methods=['GET' , 'POST'])
# def login():
#     if request.method=='POST':

app.run(debug=True)
