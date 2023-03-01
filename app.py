import prefix

from flask import Flask, url_for, request
from flask import render_template

# create app to use in this Flask application
app = Flask(__name__)

# Run just as you would lab6!
# flask --app app.py run
# https://coding.csel.io/user/<username>/proxy/5000/
prefix.use_PrefixMiddleware(app)   

@app.route('/')
def index():
    return render_template('whatchawatchin.html')

