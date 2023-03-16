## SQL Tables
  * Login information
  * User profile
  * Movies

## Login Informatoin
### Table Description
  * Table will contain username key and corresponding password that will be used to verify a valid login
### Table Columns
  * UserID - unique id for user to be used for login
  * Password - string that will be used to verify a valid login corresponding to username
### Tests
  *
  *
  *
  
## User profile
### Table Description
  * Table will contain each user's saved movie information
### Table Columns
  * IDUser - unique id for user
  * WatchedMovies - List of movies that the user has already watched
  * ToWatch - LIst of movies that the user wants to watch
  * LikedMovies - List of movies that the user has watched and liked
  * DislikedMovies - List of movies that the user has watched and disliked
### Tests
  *
  *
  *
  
## Movies
### Table Description
  * Table that will contain movies and movie information
### Table Columns
  * MovieID - Unique id for each movie
  * Title - Name of movie
  * Genres - List of genres that a movie falls into
  * Runtime - Length of movie in minutes
  * Langauge - The langauge the movie is in
  * Ratings - The average ratings that users have given it on IMDB
  *
  *
### Tests
  *
  *
  *
---
---
## Access Methods
### Access 1
 * Create user
   * Verify unique user name with corresponding password
 * Description
   * Test the create user page
 * Pre-conditions
   * User made unique user name with a password
 * Test Steps
   1. Navigate to create user page
   2. Provide valid and unique user name
   3. Provide valid password
   4. Click create user button
 * Expected Result
   * User had been created and added to the database
 * Actual Result
   * Web page displays notification indicating successful user creation
 * Status
   * Pass
 * Notes
   * N/A
 * Post-conditions
   * User is created and added to the database
 
 ### Access 2
