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
  * When adding to db check that username is unique
  * Username criteria
  * Password criteria
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
  * When trying to movie to list check for duplicates
  * Check that movies in LikedMovies aren't in DislikedMovies and visversa
  * Reference the Login Information table to ensure the user is valid.
  * Reference the Movies table to ensure the movie is valid. 
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
  * MovidID unique
  * No movie duplicates
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
 * Login User
   * Verifiy login with valid user name and password
 * Description
   * Test the login page
 * Pre-conditions
   * User has valid user name and password
 * Test Steps
   1. Navigate to login page
   2. Input valid user name
   3. Input valid password
   4. Click login button
 * Expected Result
   * User has been logged in 
 * Actual Result
   * User is navigated to user profile page
 * Status
   * Pass
 * Notes
   * N/A
 * Post-conditions
   * User is validated within database and signed into their account.
 
 ### Access 3
 * Individual Movie Data
 
 ### Access 4
 * Movie Search Results
 
 ### Access 5
 * User Profile Information 
