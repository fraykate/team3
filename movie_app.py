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

# reads database for corresponding user
@app.route('/profile')
def user_profile():
    file = "movie_app.db"
    user = "admin"
    conn = sqlite3.connect(file)
    cur = conn.cursor()
    
    user_likes = []
    user_dislikes = []
    user_watched = []
    user_towatch = []
    
    for likesid in cur.execute("SELECT Likes FROM likes WHERE IDUser='"+ user +"';"):
        #for like_movie_name in cur.execute("SELECT title FROM movies WHERE MovieID='" + likes + "';"):
        user_likes.append(likesid) #, like_movie_name)
    
    for dislikesid in cur.execute("SELECT Dislikes FROM dislikes WHERE IDUser='"+ user +"';"):
        user_dislikes.append(dislikesid)
        
    for watchedid in cur.execute("SELECT Watched FROM watched WHERE IDUser='"+ user +"';"):
        user_watched.append(watchedid)
        
    for towatchid in cur.execute("SELECT ToWatch FROM toWatch WHERE IDUser='"+ user +"';"):
        user_towatch.append(towatchid)
        
    conn.close
    return render_template('userprofile.html', user_likes = user_likes, user_dislikes = user_dislikes, user_watched = user_watched, user_towatch = user_towatch)


#Login placeholder 
@app.route('/login')
def login():
    return 'login'
# Movie detail page for titanic
@app.route('/search/movie/titanic')
def titanic():
    return render_template("search.html")

# Movie detail page for Alfie
@app.route('/search/movie/alfie')
def alfie():
    return render_template("search.html")

# Movie detail page for twilight
@app.route('/search/movie/twilight')
def twilight():
    return render_template("search.html")
     

###############################################################################
# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server using port 3308 instead of port 5000.
    app.run(host='0.0.0.0', port=3308)


# conn.commit()
# conn.close()
