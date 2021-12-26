# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_app]
# [START gae_python3_app]

# Setting virtual environment: $ python -m venv env
#                              $ .\env\Scripts\activate

# Following this tutorial
# https://cloud.google.com/appengine/docs/standard/python3/quickstart#windows
# Google Cloud project id: helloworld-335910
# Google Cloud project number: 578935054569

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
