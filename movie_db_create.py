#!/usr/bin/python3

##############################################################
# THIS IS THE FILE FOR CREATING AND FILLING THE DATABASE

# Contributing Authors: Kate Fray, Ray Franco
##############################################################

import sqlite3
import sys
import csv
import re
# TODO - may want to get rid of this
import random


dbname = 'movie_app.db'

#TODO - Clean this up, this is the formatting necessary for importing IMDB files, still a WIP
# with open("data/title.basics.tsv", 'r') as myfile: 
#   with open("data/title.basics.csv", 'w') as csv_file:
#     for line in myfile:
#       fileContent = re.sub("\t", ",", line)
#       csv_file.write(fileContent)

# Create Function: Create a db with the filename given
def create(dbname):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    # Create the titleBasics table
    c.execute("CREATE TABLE titleBasics(tconst VARCHAR, language VARCHAR, titleType VARCHAR, primaryTitle VARCHAR, originalTitle VARCHAR, isAdult NUMERIC, startYear NUMERIC, endYear NUMERIC, runtimeMinutes NUMERIC, genres VARHAR, averageRating NUMERIC,numVotes NUMERIC);")
    
    # Create titleDetails table
    c.execute("CREATE TABLE titleDetails (tconst VARCHAR, posterUrl VARCHAR, review VARCHAR);")

    #KF added Likes and IDUser - wasn't working until I added this but maybe there's something else that was supposed to happen?
    # Create likes table
    c.execute("CREATE TABLE likes (username VARCHAR, movieid VARCHAR, Likes NUMERIC, IDUser NUMERIC);")

    #KF added Dislikes and IDUser - wasn't working until I added this but maybe there's something else that was supposed to happen?
    # Create dislikes table
    c.execute("CREATE TABLE dislikes (username VARCHAR, movieid VARCHAR, Dislikes NUMERIC, IDUser NUMERIC);")

    #KF added Watched and IDUser - wasn't working until I added this but maybe there's something else that was supposed to happen?
    # Create watched table
    c.execute("CREATE TABLE watched (username VARCHAR, movieid VARCHAR, Watched NUMERIC, IDUser NUMERIC);")

    #KF added ToWatch and IDUser - wasn't working until I added this but maybe there's something else that was supposed to happen?
    # Create to_watch table
    c.execute("CREATE TABLE to_watch (username VARCHAR, movieid VARCHAR, ToWatch NUMERIC, IDUser NUMERIC);")

    # Create Login table
    c.execute("CREATE TABLE login (username VARCHAR, password VARCHAR)")



    conn.commit()
    conn.close()

# Fill Function: Fill the created tables with data
def fill(dbname):
    conn = sqlite3.connect(dbname) 
    c = conn.cursor()
    
    # FILL THE titleBasics TABLE
    file = open('data/movies.csv')
    contents = csv.reader(file)
    
    # SQL query to insert data into the basics table
    insert_records = "INSERT INTO titleBasics (tconst, language, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres, averageRating, numVotes) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)" 
    # Importing the contents of the file into the table
    c.executemany(insert_records, contents)
    
    # close file
    file.close()

    # FILL THE titleDetails TABLE
    file = open('data/movies_detail.csv')
    contents = csv.reader(file)
    
    # SQL query to insert data into the details table
    insert_records = "INSERT INTO titleDetails (tconst, posterUrl, review) VALUES(?, ?, ?)" 
    # Importing the contents of the file into the table
    c.executemany(insert_records, contents)
    
    # close file
    file.close()

    # Let's add at least on user for now;
    c.execute("INSERT INTO login (username, password) VALUES ('admin', 'password')")

    conn.commit()
    conn.close()

#TODO - just a placeholder for add user
def addUser(dbname, userName, email):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    c.execute("INSERT INTO User VALUES (?, ?);", (userName, email))

    conn.commit()
    conn.close()



def main():

    create(dbname)
    fill(dbname)
    #  addUser(dbname,productName, price, categoryID, description)

## only call main if this file is run directly 
## otherwise skip main so it can be imported in other 
## python scripts
if __name__ == "__main__":
    main()



