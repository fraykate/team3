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
    c.execute("CREATE TABLE titleBasics(tconst VARCHAR PRIMARY KEY, titleType VARCHAR, primaryTitle VARCHAR, originalTitle VARCHAR, isAdult NUMERIC, startYear NUMERIC, endYear NUMERIC, runtimeMinutes NUMERIC, genre1 TEXT DEFAULT 'abc', genre2 TEXT DEFAULT 'abc', genre3 TEXT DEFAULT 'abc');")

    # Create likes table
    c.execute("CREATE TABLE likes (username VARCHAR, movieid VARCHAR);")

    # Create dislikes table
    c.execute("CREATE TABLE dislikes (username VARCHAR, movieid VARCHAR);")

    # Create watched table
    c.execute("CREATE TABLE watched (username VARCHAR, movieid VARCHAR);")

    # Create to_watch table
    c.execute("CREATE TABLE to_watch (username VARCHAR, movieid VARCHAR);")

    # Create Login table
    c.execute("CREATE TABLE login (username VARCHAR, password VARCHAR)")



    conn.commit()
    conn.close()

# Fill Function: Fill the created tables with data
def fill(dbname):
    conn = sqlite3.connect(dbname) 
    c = conn.cursor()
    
    # FILL THE titleBasics TABLE (right now it's pointing at a dummy file)
    file = open('data/movies.csv')
    contents = csv.reader(file)
    
    # TODO - Part of the issue with varying columns in csv file, still a WIP
    # SQL query to insert data into the person table
    insert_records = "INSERT INTO titleBasics (tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genre1) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)" 
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



