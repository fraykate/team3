import prefix

from flask import Flask, url_for, request
from flask import render_template

# create app to use in this Flask application
app = Flask(__name__)

# Insert the wrapper for handling PROXY when using csel.io virtual machine
# Calling this routine will have no effect if running on local machine
prefix.use_PrefixMiddleware(app)   

@app.route('/')
def index():
    return render_template('whatchawatchin.html')

