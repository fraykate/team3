#!/usr/bin/python3

##############################################################
# THIS IS THE FLASK APP FOR ROUTING

# To run this, activate your python venv
# $ export FLASK_APP=movie_app.py
# $ flask run --debug

# Contributing Authors: Kate Fray
##############################################################

import prefix
import sqlite3
from flask import Flask, url_for, render_template
from markupsafe import escape


# create app to use in this Flask application
app = Flask(__name__)

# Connect to the movies.db database
conn = sqlite3.connect('movie_app.db', check_same_thread=False)
c = conn.cursor()

# Insert the wrapper for handling PROXY when using csel.io virtual machine
# Calling this routine will have no effect if running on local machine
prefix.use_PrefixMiddleware(app)   

# THIS IS A DUMMY INDEX PAGE
# TODO - Chris I don't know if we want to add my route to your file or yours to this, we can figure that out
@app.route('/')  
def index():
    resp =  ''' 
            <html>
            <link rel="stylesheet" href="static/css/myflaskapp.css">
             <div>
                 Watchawatchin?!
            </div><br><hr><br>
            Top Selling Movie:
             '''
    # TODO - We will need to figure out how to handle passing the searched movie into the moviename variable
    movie_url = url_for("show_movie_profile", moviename='Twilight')
    resp +=  '<a href="' + movie_url + '" > Twilight</a>'
    return resp

# THIS IS THE ROUTE FOR THE MOVIE DETAILS PAGE
# TODO - How to use this route from another page, probably the movie category page
# TODO - Need to pass a user selection into <moviename>
@app.route('/<moviename>')
def show_movie_profile(moviename):
    fetch = "SELECT * FROM titleBasics WHERE primaryTitle = '" + moviename + "'" 
    c.execute(fetch)
    data = c.fetchall()
    return render_template("movie_detail.html", moviename=moviename, data=data)



###############################################################################
# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server using port 3308 instead of port 5000.
    app.run(host='0.0.0.0', port=3308)


# conn.commit()
# conn.close()
