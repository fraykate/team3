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

################################
## Functions for likes table ###
################################

# Function: addLike
# Description: Records a user's like to the database
# Parameters: username, movie_id 
# Returns: Nothing
def addLike(username, movie_id, database = dbname):
    addGeneric("likes", username, movie_id, database)


# Function: removeLike
# Description: removes a user's like from the database
# Parameters: username, movie_id 
# Returns: Nothing
def removeLike(username, movie_id, database = dbname):
    removeGeneric("likes", username, movie_id, database)


# Function: countLikesByUser
# Description: Counts the total number of likes for a user
# Parameters: username
# Returns: number of user likes
def countLikesByUser(username, database = dbname):
    return countGenericByUser("likes", username, database)

# Function: countLikesByMovie
# Description: Counts the total number of likes for a movie
# Parameters: movie_id
# Returns: number of movie likes
def countLikesByMovie(movie_id, database = dbname):
    return countGenericByMovie("likes", movie_id, database)

# Function: isMovieLikedByUser
# Description: Checks to see if the user has already liked the movie
# Parameters: username, movie_id
# Returns: returns true if the movie has already been liked by the user
#          otherwise returns false
def isMovieLikedByUser(username, database = dbname):
    return isMovieGenericByUser("likes", username, database)


#################################
## Functions for watched table ##
#################################

# Function: addWatched
def addWatched(username, movie_id, database = dbname):
    addGeneric("watched", username, movie_id, database)


# Function: removeWatched
# Parameters: username, movie_id 
# Returns: Nothing
def removeWatched(username, movie_id, database = dbname):
    removeGeneric("watched", username, movie_id, database)


# Function: countWatchedByUser
# Parameters: username
# Returns: number of movies user has seen
def countWatchedByUser(username, database = dbname):
    return countGenericByUser("watched", username, database)

# Function: countWatchedByMovie
# Parameters: movie_id
# Returns: number of time a movie has been watched by users
def countWatchedByMovie(movie_id, database = dbname):
    return countGenericByMovie("watched", movie_id, database)

# Function: isMovieWatchedByUser
# Description: Checks to see if the user has already seen the movie
# Parameters: username, movie_id
# Returns: returns true if the movie has already been seen by the user
#          otherwise returns false
def isMovieWatchedByUser(username, database = dbname):
    return isMovieGenericByUser("watched", username, database)

## The following code is reused by other functions.
## TODO change to scope of these functions so that they 
## can only be used by functions in this file.
def addGeneric(table, username, movie_id, database):
    conn = sqlite3.connect(database)
    c = conn.cursor()

    c.execute('INSERT INTO %s (username, movieid) VALUES (?,?)'%table, (username, movie_id))
    conn.commit()
    conn.close()  

def removeGeneric(table, username, movie_id, database = dbname):
    conn = sqlite3.connect(database)
    c = conn.cursor()

    c.execute("DELETE FROM %s WHERE username = (?) AND movieid = (?)"%table, (username, movie_id))
    conn.commit()
    conn.close()

def countGenericByUser(table, username, database = dbname):
    conn = sqlite3.connect(database)
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM %s WHERE username = (?) "%table, (username,))
    ret = c.fetchall()

    conn.commit()
    conn.close()

    return ret[0][0]

def countGenericByMovie(table, movie_id, database = dbname):
    conn = sqlite3.connect(database)
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM %s WHERE movieid = (?) "%table, (movie_id,))
    ret = c.fetchall()

    conn.commit()
    conn.close()

    return ret[0][0]

def isMovieGenericByUser(table, username, database = dbname):
    ret = True
    conn = sqlite3.connect(database)
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM %s WHERE username = (?) "%table, (username,))
    count = c.fetchall()

    conn.commit()
    conn.close()

    if count[0][0] == 0:
        ret = True
    else:
        ret = False

    return ret