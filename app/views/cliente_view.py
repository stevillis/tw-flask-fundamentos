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
