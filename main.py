# THE LINK TO THE RUNNING APP:  https://helloworld-335910.ew.r.appspot.com/

from flask import Flask
from markupsafe import escape


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return """
    <h1  style='color: blue;'>Hello World!</h1>
    <p>Is the anybody out there?</p>
    <p>I hope you can see me...</p>
    <code style="font-size: 1rem">That's me, <em>Mark Kirzhner</em></code>
    """


@app.route('/about')
def about():
    """Return a friendly HTTP greeting."""
    return "<h1>Welcome to <span style='color: blue;'>THE ABOUT!!!</span></h1>"


@app.route('/welcome/<name>')
def welcome(name):
    return f"""<h2>Hello dear <span style='font-size: 2rem; color: blue;'> {escape(name)}</span>, welcome to the welcome page.</h2>"""


@app.errorhandler(404)
def invalid_route(e):
    return "<h1>404 page - <span style='color: blue;'>Unrecognized rout</span></h1>"


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]
