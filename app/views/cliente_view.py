"""Cliente view."""

from app import app


@app.route('/hello')
def hello():
    """Hello world view."""
    return 'Hello, world from Flask!'
