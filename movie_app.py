#!/usr/bin/python3

##############################################################
# THIS IS THE FLASK APP FOR ROUTING

# To run this, activate your python venv
# $ export FLASK_APP=movie_app.py
# $ flask run --debug

# Contributing Authors: Kate Fray
#                       Chris Lescinskas 
##############################################################

import prefix
import sqlite3
from flask import Flask, url_for, render_template, request
from markupsafe import escape
import sys
sys.path.insert(1, './movie_db_api/')
import movie_db_api as dbAPI


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
    fetch = "SELECT DISTINCT(genres) FROM titleBasics LIMIT 4"
    c.execute(fetch)
    data = c.fetchall()
    return render_template('whatchawatchin.html', data=data)



#Populates the searh page
@app.route('/search/')
def search_movie():
    return render_template("search.html")

#Receive user input from search page via POST
@app.route('/search/movie/', methods=['POST', 'GET'])
def show_movie_profile():
    #Get user data from POST
    moviename = request.form['movie_name']
    #Query db using title provided by user
    fetch = "SELECT * FROM titleBasics LEFT JOIN titleDetails ON titleBasics.tconst = titleDetails.tconst WHERE primaryTitle = '" + moviename + "'" 
    c.execute(fetch)
    data = c.fetchall()
    #If movie not found, populate that template 
    if len(data) == 0:
        return render_template("movie_not_found.html")
    else:
        return render_template("movie_detail.html", moviename=moviename, data=data)

# reads database for corresponding user
@app.route('/profile')
def user_profile(user = None):
    fetch = "SELECT * FROM login" 
    c.execute(fetch)
    data = c.fetchall()

    file = "movie_app.db"
    #should comment out below line for demo?
    #user = "admin"
    conn = sqlite3.connect(file)
    cur = conn.cursor()
    
    try: 
        with open('login.txt') as f:
            lines = f.readlines()
            user = lines[0]
    except:
        print("user not logged in or file not found")
    
    user_likes = []
    user_dislikes = []
    user_watched = []
    user_towatch = []
    if user != None:
        for likesid in cur.execute("SELECT Likes FROM likes WHERE IDUser='"+ user +"';"):
            #for like_movie_name in cur.execute("SELECT title FROM movies WHERE MovieID='" + likes + "';"):
            user_likes.append(likesid) #, like_movie_name)

        for dislikesid in cur.execute("SELECT Dislikes FROM dislikes WHERE IDUser='"+ user +"';"):
            user_dislikes.append(dislikesid)

        for watchedid in cur.execute("SELECT Watched FROM watched WHERE IDUser='"+ user +"';"):
            user_watched.append(watchedid)

        for towatchid in cur.execute("SELECT ToWatch FROM to_watch WHERE IDUser='"+ user +"';"):
            user_towatch.append(towatchid)

    conn.close
    return render_template('userprofile.html', user_likes = user_likes, user_dislikes = user_dislikes, user_watched = user_watched, user_towatch = user_towatch, user = user, data = data)


@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/login_attempt', methods=['POST', 'GET'])
def login_attempt():
    username = request.form['username']
    password = request.form['password']
    ret = dbAPI.loginUser(username, password, "./movie_app.db")
    if ret:
        f = open("login.txt", "w")
        f.write(username)
        f.close()
        return render_template("login_user_true.html", username=username)
    else:
        return render_template("login_user_failed.html", username=username)

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/attempt', methods=['POST', 'GET'])
def attempt():
    username = request.form['username']
    password = request.form['password']
    ret = dbAPI.addUser(username, password, "./movie_app.db")
    if ret:
        return render_template("create_user_true.html", username=username)
    else:
        return render_template("create_user_failed.html", username=username)

# Movie detail page for titanic
@app.route('/search/movie/titanic')
def titanic():
    return render_template("movie_detail_titanic.html")

# Movie detail page for Alfie
@app.route('/search/movie/alfie')
def alfie():
    return render_template("movie_detail_alfie.html")

# Movie detail page for twilight
@app.route('/search/movie/twilight')
def twilight():
    return render_template("movie_detail_twilight.html")
     

###############################################################################
# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server using port 3308 instead of port 5000.
    app.run(host='0.0.0.0', port=3308)


# conn.commit()
# conn.close()
