#!/usr/bin/python3

##############################################################
# THIS IS THE FILE FOR CREATING AND FILLING THE DATABASE

# Contributing Authors: Kate Fray
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

    # TODO - create the subsequent needed tables

    conn.commit()
    conn.close()

# Fill Function: Fill the created tables with data
def fill(dbname):
    conn = sqlite3.connect(dbname) 
    c = conn.cursor()
    
    # FILL THE titleBasics TABLE (right now it's pointing at a dummy file)
    file = open('data/dummymovies.csv')
    contents = csv.reader(file)
    
    # TODO - Part of the issue with varying columns in csv file, still a WIP
    # SQL query to insert data into the person table
    insert_records = "INSERT INTO titleBasics (tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genre1) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)" 
    # Importing the contents of the file into the table
    c.executemany(insert_records, contents)
    
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

main()



