from flask import render_template
from sophia import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/relatorios')
def relatorios():
    return render_template('relatorios.html')


@app.route('/login')
def login():
    return render_template('login.html')
