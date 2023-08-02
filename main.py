from flask import (Flask,
                   render_template,
                   request,
                   session,
                   redirect,
                   url_for)
from dotenv import load_dotenv
import flask_session
from auth_lib import login_manager
from flask_login import login_required
from models import db
from models import User
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from auth_part import auth_app
from wtforms_alchemy import ModelForm
from flask_login import login_user

import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]
app.config["SESSION_TYPE"] = os.environ["SESSION_TYPE"]
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DB"]
flask_session.Session(app)

db.init_app(app)
with app.app_context():
    db.create_all()

login_manager.init_app(app)


class UserForm(ModelForm):
    class Meta:
        model = User


@app.route('/login', methods=["POST", 'GET'])
def login():
    form = UserForm()
    if request.method == "POST":
        form.data = request.form

        # user = User.query\
        #        .filter(User.login == form.data.get("login")) \
        #        .filter(User.password == form.data.get("password"))\
        #        .first()
        #
        # login_user(user)

        return render_template("/login.html",
                               form=form)


@app.route("/")
@login_required
def index():
    return render_template("page.html")


app.register_blueprint(auth_app)

admin = Admin(app, name='Tasks21', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))

app.run()
