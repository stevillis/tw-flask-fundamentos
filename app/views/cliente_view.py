"""Cliente view."""

from app import app
from flask import render_template


@app.route('/hello')
def hello():
    """Hello world view."""
    return 'Hello, world from Flask!'


@app.route('/welcome/<string:name>')
def welcome(name):
    """Route with mandatory parameter."""
    return f'Welcome {name}!'


@app.route('/goodmorning', defaults={'name': None})
@app.route('/goodmorning/<string:name>')
def good_morning(name):
    """Route with optional parameter."""
    if name:
        return f'Good morning, {name}!'
    return 'Good morning!'


@app.route('/bank', methods={'DELETE'})
def bank():
    """Route with specific HTTP method."""
    return 'Contente deleted!'


@app.route('/<string:name>', methods={'GET'})
def home(name):
    """Home view."""
    return render_template('clientes/home.html', user_name=name)
