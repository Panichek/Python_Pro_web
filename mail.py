from flask import Flask
from flask_mail import Mail
from flask_mail import Message

app = Flask(__name__)


app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "egen11112222@gmail.com"
app.config["MAIL_PASSWORD"] = "wjudmudlvorugzfm"
mail = Mail(app)

msg = Message("Hello From Site",
              sender="egen11112222@gmail.com",
              body = "Привіт світ",
              recipients=["panichek@ukr.net"])
with app.app_context():
    mail.send(msg)
