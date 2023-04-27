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
        dbCreate.create(testdb)
        dbCreate.fill(testdb)

    def tearDown(this): 
        os.remove('my_test.db')


    ## Login test 1: Check for table
    ## Description: Check to see if database contains table for user information
    def test_login_1(self):
        # we should be able to see if the table exists if we query it
        conn = sqlite3.connect(testdb)
        c = conn.cursor()

        c.execute("SELECT 'ping' FROM login LIMIT 1")
        ret = c.fetchall()

        conn.commit()
        conn.close()

        self.assertEqual(ret[0][0], 'ping')


    ## Login test 2: Adding User Valid Criteria Check 
    ## Description: Create a user with a valid user name and password, and add to login information table
    def test_login_2(self):
         ## Valid Username and password
         self.assertTrue(dbAPI.addUser('ray', '12345678', testdb))
         ## username is too short
         self.assertFalse(dbAPI.addUser('ra', '12345678', testdb))
         ## password is too short
         self.assertFalse(dbAPI.addUser('jake', '1234567', testdb))
         ## Username and password is too short
         self.assertFalse(dbAPI.addUser('ja', '12', testdb))
         ## Username cannot have a space in it
         self.assertFalse(dbAPI.addUser('jake doe', 'this_password_is_ok', testdb))
         ## Password cannot have a space in it
         self.assertFalse(dbAPI.addUser('hello', 'not okay', testdb))

         ## For fun let's add some more valid users
         self.assertTrue(dbAPI.addUser('tim', 'password', testdb))
         self.assertTrue(dbAPI.addUser('lilly', 'password123', testdb))
         self.assertTrue(dbAPI.addUser('megaman', 'password_!!', testdb))

         ## Usernames cannot be the same
         self.assertFalse(dbAPI.addUser('tim', 'diff_password', testdb))
         self.assertFalse(dbAPI.addUser('megaman', 'password_!!', testdb))

if __name__ == '__main__':
    unittest.main()