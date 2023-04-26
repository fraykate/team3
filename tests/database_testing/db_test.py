#!/bin/python3

##############################################################
# THIS IS THE FILE FOR TESTING DATABASE API

# Contributing Authors: Ray Franco
##############################################################

import sys
sys.path.insert(1, '../../movie_db_api/')
sys.path.insert(1, '../../')
import movie_db_api as dbAPI
import movie_db_create as dbCreate
import unittest
import os
import sqlite3


dbAPI.addLike("ray", 1234, "../../movie_app.db")
dbAPI.addLike("ray", 8460, "../../movie_app.db")
dbAPI.addLike("ray", 7888, "../../movie_app.db")


dbAPI.removeLike("ray", 7888, "../../movie_app.db")


dbAPI.countLikesByUser("ray", "../../movie_app.db")

dbAPI.countLikesByMovie(7888, "../../movie_app.db")

testdb = "my_test.db"

class WidgetTestCase(unittest.TestCase):
    def setUp(this):
        print("Creating test database called my_test.db")
        dbCreate.create(testdb)
        print("...loading my_test.db")
        dbCreate.fill(testdb)

    def tearDown(this): 
        print("Removing my_test.db")
        os.remove('my_test.db')

    ## Login test 1: Check for table
    ## Description: Check to see if database contains table for user information
    def test1(self):
        # we should be able to see if the table exists if we query it
        conn = sqlite3.connect(testdb)
        c = conn.cursor()

        c.execute("SELECT 'ping' FROM login LIMIT 1")
        ret = c.fetchall()

        conn.commit()
        conn.close()

        print(ret)
        self.assertEqual(ret[0][0], 'ping')


    ## Login test 2: Adding User Valid Criteria Check 
    ## Description: Create a user with a valid user name and password, and add to login information table
    def test2(self):
         print("todo")

if __name__ == '__main__':
    unittest.main()