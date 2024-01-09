from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/login')
def login():
    return "LOGIN PAGE"

app.run(debug = True)