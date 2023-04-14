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
  * Test 1: Check for table
    * Use case name: "Check/Create Table"
    * Description: Check to see if database contains table for user information
    * Pre-conditions:
      * Login information database not created
    * Test Steps
      * Check that table exists
        * If table doesn't exist then make one
        * If it does exist return that table is present
    * Expected Results
      * Login information database exist
    * Actual Results
      * Receive message saying database is created or present
    * Status: Pass
    * Notes: n/a
    * Post-conditions: n/a
  * Test 2: Adding User Valid Criteria Check
    * Use case name: "Valid Entry"
    * Description: Create a user with a valid user name and password, and add to login information table
    * Pre-conditions:
      * The login information table is created
    * Test Steps
      * Check that created username is minimum 3 characters with no white spaces
      * Check that password is minimum 8 characters with no white spaces
      * With created username iterate through table to see if username exists
        * If username doesn't exist add new user and password information to table, otherwise return error 
    * Expected Results
      * New user added to database
    * Actual Results
      * Feedback given that user is added to database
    * Status: Pass
    * Notes: n/a
    * Post conditions: n/a
### Page Descriptions
  * The Login page will xyz
  * In order to validate the data is correct we will xyz
---  
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
  * Reference the Login Information table to ensure the user is valid.
  * Reference the Movies table to ensure the movie is valid. 
  * Test 1: Check user profile is valid
    * Use case name: "Valid Profile"
    * Description: When in profile page check that a valid user is logged in
    * Pre-conditions:
      * User is logged in
      * Login information table is present
      * User profile table is present
    * Test Steps
      * Iterate through Login information table and profile table
      * Check to see user is present in both tables
        * If user isn't present return error message, otherwise continue to profile page
    * Expected Results
      * User profile present
    * Actual Results
      * User able to go into profile page
    * Status: Pass
    * Notes: n/a
    * Post conditions: n/a
  * Test 2: Check for Valid Movie
    * Use case name: "Valid Movie"
    * Description: Before adding movie to Liked or Disliked Table check that the movie matches a movie in database
    * Pre-conditions:
      * User is logged in
      * Movie database present
    * Test Steps
      * Iterate through movie table and check to see if movie is matches id in database
        * If movie not present return error, if present continue to intended action ()
    * Expected Results
      * Movie present
    * Actual Results
      * Log that movie is present in database
    * Status: Pass
    * Notes: n/a
    * Post conditions: n/a
  * Test 3: Adding Movie to LikedMovies table
    * Use case name: "Added Liked Movie"
    * Description: Add movie to user profiles LikedMovies Table
    * Pre-conditions:
      * User is logged in
      * User profile table is present
    * Test Steps
      * Iterate through user's LikedMovies and DislikedMovies Table
      * Check to see if movie is present in either list
        * If movie doesn't exist in either list add to LikedMovies table
        * If movie exists in DislikedMovies table
          * Delete movie from Disliked Movies, add to LikedMovies and return moved from disliked to liked message
        * If movie exists in LikedMovies table return movie already in table error
    * Expected Results
      * Movie added to LikedTable
    * Actual Results
      * Feedback given that movie is added to LikedMovies
    * Status: Pass
    * Notes: n/a
    * Post conditions: n/a
  * Test 4: Adding Movie to DislikedMovies table
    * Use case name: "Added Disliked Movie"
    * Description: Add movie to user profiles DislikedMovies Table
    * Pre-conditions:
      * User is logged in
      * User profile table is present
    * Test Steps
      * Iterate through user's LikedMovies and DislikedMovies Table
      * Check to see if movie is present in either list
        * If movie doesn't exist in either list add to DislikedMovies table
        * If movie exists in LikedMovies table
          * Delete movie from Liked Movies, add to DislikedMovies and return moved from liked to disliked message
        * If movie exists in DisikedMovies table return movie already in table error
    * Expected Results
      * Movie added to DislikedTable
    * Actual Results
      * Feedback given that movie is added to DislikedMovies
    * Status: Pass
    * Notes: n/a
    * Post conditions: n/a
---  
## Movies
### Table Description
  * Table that will contain movies and movie information
  * This will a dynamic table, nothing can be added or changed after the initial creation
  * It will be used by individual movie and search results html pages to access information
### Table Columns
  * MovieID - Unique id for each movie
  * Title - Name of movie
  * Genres - List of genres that a movie falls into
  * Runtime - Length of movie in minutes
  * Langauge - The langauge the movie is in
  * Ratings - The average ratings that users have given it on IMDB

### Tests
  * Test 1: Check for Movie Duplicates
    * Use case name: "No Duplicates"
    * Description: Check to see if there are any duplicate movie ids
    * Pre-conditions:
      * The movie database table is created
    * Test Steps
      * Iterate through movie ids
        * If duplicates exist delete the ones after the first one found, otherwise return no duplicates 
    * Expected Results
      * No duplicates found
    * Actual Results
      * Log that there are no duplicates/movie database is good
    * Status: Pass
    * Notes: n/a
    * Post conditions: n/a
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
