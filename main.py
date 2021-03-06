from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/add/<string:newstring>')
def add(newstring):
    """Return a friendly HTTP greeting."""
    return '# ' + newstring


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'This page left intentionally blank.', 404
