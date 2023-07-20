from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/route1')
def route1():
    return '1'

@app.route('/route2')
def route2():
    return '2'

@app.route('/route3')
def route3():
    return '3'

@app.route('/route4')
def route4():
    return '4'

@app.route('/route5')
def route5():
    return '5'

app.run()
