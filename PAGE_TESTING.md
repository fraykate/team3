## Website Pages
  * Main/Home Page
  * Log in Page
  * Create User Page (could be on the same as the log in page?)
  * Movie Results Page
  * Movie Information Page
  * User Profile Page
  
## Main/Home Page
### Page Description (include a mockup or hand drawn image of the page)
### Parameters needed for the page
### Data needed to render the page
### Link destinations for the page
### List of tests for verifying the rendering of the page

## Login Page
### Page Description (include a mockup or hand drawn image of the page)
* This page will allow the user to login. 
### Parameters needed for the page
* None
### Data needed to render the page
* The User's username if logged in.
### Link destinations for the page
* ./login
### List of tests for verifying the rendering of the page
* If the user is already logged in. Redirect to User Profile Page. 

## Create User Page
### Page Description (include a mockup or hand drawn image of the page)
* This page will allow a user to create a new account. 
### Parameters needed for the page
* None
### Data needed to render the page
* The User's username if logged in.
### Link destinations for the page
* ./create_account
### List of tests for verifying the rendering of the page
* If the user is already logged in. Redirect to User Profile Page. 

## Movie Results Page
### Page Description (include a mockup or hand drawn image of the page)
### Parameters needed for the page
### Data needed to render the page
### Link destinations for the page
### List of tests for verifying the rendering of the page

## Movie Information Page
### Page Description (include a mockup or hand drawn image of the page)
### Parameters needed for the page
### Data needed to render the page
### Link destinations for the page
### List of tests for verifying the rendering of the page

## User Profile Page
### Page Description 
* This Page will show a users created profile page
* It will show a list of movies they want to watch
* It will also show lists for liked and disliked movies that they have already watched.
![userprofilepage](https://user-images.githubusercontent.com/83556347/225323812-d054b6fe-8a81-4f4c-8ab0-d0bdd4c53933.png)
### Parameters needed for the page
* User needs to be logged in to view page
* User needs to have movies added to watch,liked,dislike list to view corresponding lists
### Data needed to render the page
* The user's username
* List from database of movies they want to watch
* List from database of movies they liked
* List from database of movies they disliked
### Link destinations for the page
* ./username
### List of tests for verifying the rendering of the page
* Verify username displayed matches the same username that was used to login 
* Verify movie lists are displaying correctly at that what's shown matches list in database related to username
