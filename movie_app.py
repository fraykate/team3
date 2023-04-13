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
from flask import Flask, url_for, render_template, request
from markupsafe import escape


# create app to use in this Flask application
app = Flask(__name__)

# Connect to the movies.db database
conn = sqlite3.connect('movie_app.db', check_same_thread=False)
c = conn.cursor()

# Insert the wrapper for handling PROXY when using csel.io virtual machine
# Calling this routine will have no effect if running on local machine
# prefix.use_PrefixMiddleware(app)   

@app.route('/')  
def homepage():
    fetch = "SELECT genre1 FROM titleBasics LIMIT 4"
    c.execute(fetch)
    data = c.fetchall()
    return render_template('whatchawatchin.html', data=data)



#This is meant to be a dummy page to explore passing variable into route
#Eventually this will be replaced by genre 
@app.route('/search/')
def search_movie():
    return render_template("search.html")


@app.route('/search/movie/', methods=['POST', 'GET'])
def show_movie_profile():
    moviename = request.form['movie_name']
    ## How do we handle movies that aren't in databse?
    ## How do we handle movies with the same name?
    fetch = "SELECT * FROM titleBasics WHERE primaryTitle = '" + moviename + "'" 
    c.execute(fetch)
    data = c.fetchall()
    if len(data) == 0:
        return render_template("movie_not_found.html")
    else:
        return render_template("movie_detail.html", moviename=moviename, data=data)



###############################################################################
# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server using port 3308 instead of port 5000.
    app.run(host='0.0.0.0', port=3308)


# conn.commit()
# conn.close()
