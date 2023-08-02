from flask import Blueprint, render_template

auth_app = Blueprint('auth_app', __name__,
                     template_folder='templates')



# @auth_app.route("/login")
# def login():
#     user = User.query.first()
#     login_user(user)
#     return "увійшли"
