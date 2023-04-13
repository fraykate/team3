## SQL Tables
  * Login information
  * User profile
  * Movies

## Login Information
### Table Description
  * Table will contain username key and corresponding password that will be used to verify a valid login
  * It will be used by the log in and create user html pages
### Table Columns
  * UserID - unique id for user to be used for login
  * Password - string that will be used to verify a valid login corresponding to username
### Tests
  * When adding to db check that username is unique
  * Username criteria
  * Password criteria
  * functions (name/paramters)
### Page Descriptions
  * The Login page will xyz
  * In order to validate the data is correct we will xyz
  
## User profile
### Table Description
  * The user profile will be composed of 4 different tables that can be 
  * queried indiviually or joined together. The tables are: likes, dislikes,
  * watched, and to_watch
  * It will be used by the user profile html page to view as well as the individual movie html page and search results html page to add values to user when logged in
### Table Columns
  * IDUser - unique id for user
  * WatchedMovie - Movie that the user has already watched
  * ToWatch - Movie that the user wants to watch
  * LikedMovies - Movie that the user liked
  * DislikedMovies - Movie that the user has disliked
### Tests
  * When adding a movie check for duplicates
  * Check that movies in LikedMovies aren't in DislikedMovies and visversa
  * Reference the Login Information table to ensure the user is valid.
  * Reference the Movies table to ensure the movie is valid. 
  
## Movies
### Table Description
  * Table that will contain movies and movie information
  * It will be used by individual movie and search results html pages to access information
### Table Columns
  * MovieID - Unique id for each movie
  * Title - Name of movie
  * Genres - List of genres that a movie falls into
  * Runtime - Length of movie in minutes
  * Langauge - The langauge the movie is in
  * Ratings - The average ratings that users have given it on IMDB

### Tests
  * MovidID unique
  * No movie duplicates
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
   * Verify movie informatoin with movie id
 * Description
   * Test movie information page
 * Pre-conditions
   * Movie information and movie id match
 * Test Steps
   * Select movie link
 * Expected Result
   * Movie information page filled out
 * Actual Result
   * User is navigated to movie information page
 * Status
   * Pass
 * Notes
   * N/A
 * Post-conditions
   * Movie is verified within database and displays information
 
 ### Access 4
 * Movie Search Results
   * Verify movie search results with matching criteria
 * Description
   * Test movie search results page
 * Pre-conditions
   * Movie results have matching criteria
 * Test Steps
   * Select/input search criteria
   * Click search/results button
 * Expected Result
   * List of movies given
 * Actual Result
   * User is navigated to movie search results page
 * Status
   * Pass
 * Notes
   * N/A
 * Post-conditions
   * Movies are verified within database by matching criteria
 ### Access 5
 * User Profile Information 
   * Verify user profile informatoin
 * Description
   * Test user profile page
 * Pre-conditions
   * Successful login
   * User information matched user login
 * Test Steps
   * Successfully login
   * Click user profile page button
 * Expected Result
   * User profile page filled out
 * Actual Result
   * User is navigated to user profile page
 * Status
   * Pass
 * Notes
   * N/A
 * Post-conditions
   * User profile is verified within database and displays corresponding user information
