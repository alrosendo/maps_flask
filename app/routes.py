from flask import render_template, request, redirect, url_for
from . import create_app

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mapa')
def mapa():
    return render_template('mapa.html')