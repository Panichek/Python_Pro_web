'''
На роботу із пагінацією
Створити Таблицю Record з полями name score
Створити 100000 записів записати до бази даних
Створити маршрут records який виведе записи по 20 на сторінці
'''

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "qwerty"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db = SQLAlchemy(app)


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, nullable=False)


@app.route("/records")
def get_record():
    record = db.paginate(Record.query, per_page=20)
    return render_template("records.html",
                           records=record)


if __name__ == "__main__":
    app.run()
