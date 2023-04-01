#!/usr/bin/python3

##############################################################
# This api is intended to be imported to allow simple access to 
# frequently used database commmands.  
#
# There is no main fucntion. Import into your project and make
# function calls from there. 
#
# Assumptions: The database has already been created using the 
#              movie_db_create.py script in the root of this
#              project. 
#
# Contributing Authors: Ray Franco 
##############################################################

import sqlite3
import sys

# By defult let's have all the calls effect our local version 
# of the project database. 
# If we are running unit tests we should specify another 
# database. 
dbname = 'movie_app.db'

# Database structure for reference only:
#   Tables:
#       titleBasics
#           tcont, titleType, primaryTitle, originalTitle, isAdult, startYear, 
#           endYear, runtimeMinutes, genrel, genre2, genre3
#       TBD
#



# Function: addLike
# Description: Records a user's like to the database
# Parameters: username, movie_id 
def addLike(username, movie_id, database = dbname):
    conn = sqlite3.connect(database)
    c = conn.cursor()

    c.execute("INSERT INTO likes (username, movieid) VALUES (?,?)", (username, movie_id))
    conn.commit()
    conn.close()


# Function: removeLike
# Description: removes a user's like to the database
# Parameters: username, movie_id 
def removeLike(username, movie_id, database = dbname):
    conn = sqlite3.connect(database)
    c = conn.cursor()

    c.execute("DELETE FROM likes WHERE username = (?) AND movieid = (?)", (username, movie_id))
    conn.commit()
    conn.close()

