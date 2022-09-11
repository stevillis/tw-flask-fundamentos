"""Cliente view."""

from app import app


@app.route('/hello')
def hello():
    """Hello world view."""
    return 'Hello, world from Flask!'


@app.route('/welcome/<string:name>')
def welcome(name):
    """Route with mandatory parameter."""
    return f'Welcome {name}!'
