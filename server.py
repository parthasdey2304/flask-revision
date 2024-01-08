from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<a href='/login'>LOGIN PAGE</a>"

@app.route('/login')
def login():
    return "LOGIN PAGE"

app.run(debug = True)
