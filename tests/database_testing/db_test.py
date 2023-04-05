#!/bin/python3

# TODO this should test database api
import sys
sys.path.insert(1, '../../movie_db_api/')
import movie_db_api as dbAPI


dbAPI.addLike("ray", 1234, "../../movie_app.db")
dbAPI.addLike("ray", 8460, "../../movie_app.db")
dbAPI.addLike("ray", 7888, "../../movie_app.db")


dbAPI.removeLike("ray", 7888, "../../movie_app.db")


dbAPI.countLikesByUser("ray", "../../movie_app.db")

dbAPI.countLikesByMovie(7888, "../../movie_app.db")
