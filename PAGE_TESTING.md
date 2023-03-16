## Website Pages
  * Main/Home Page
  * Log in Page
  * Create User Page (could be on the same as the log in page?)
  * Movie Results Page
  * Movie Information Page
  * User Profile Page
  
## Main/Home Page
### Page Description (include a mockup or hand drawn image of the page)!
a.	Starting point for the user experience.  Introduce users to the site and direct them towards the site’s functionalities
![Whatchawatchin HomePage MockUp](https://user-images.githubusercontent.com/78234265/225473516-ebe34cc1-4833-4a84-8afc-5835d919bca2.png)

### Parameters needed for the page
a.	None
### Data needed to render the page
a.	List of movie categories
b.	Valid link urls

### Link destinations for the page
a.	Link to user login/sign up
b.	Link for each movie category which brings us to the ‘filtering’ page for that category
c.	Link to user profile page

### List of tests for verifying the rendering of the page

a.	1 test for each link to verify it brings you to the correct location
i.	Each movie category link  filtering page for that category
ii.	Login/sign up  Page which includes the login and sign up forms
iii.	Profile  page that shows user profile
b.	1 test to verify background image and color schemes
c.	1 test to verify position of elements
i.	Profile/Login/Sign up bar  Fixed to top of page
ii.	Title  underneath Profile bar
iii.	Site Description  Below Title
iv.	Movie category links  Below Site Description


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

## Movie/Category Results Page
### Page Description (include a mockup or hand drawn image of the page)
### Parameters needed for the page
* Entered criteria
### Data needed to render the page
* Movie title, picture(if applicable), actors and actresses'name
### Link destinations for the page
* ./search_result
### List of tests for verifying the rendering of the page
* checking data includes entered criteria

## Movie Information Page
### Page Description (include a mockup or hand drawn image of the page)
* The individual page that describes the details of a chosen film/tv show/documentary/etc.
![Screenshot 2023-03-15 at 6 03 19 PM](https://user-images.githubusercontent.com/34926259/225479209-52b3922c-652d-4706-bc1b-94042e21d61d.png)


### Parameters needed for the page
* Movie ID
* Recommended Movie IDs which may be randomly generated from the genre selected, uncertain
### Data needed to render the page
* Movie Title
* Image address for movie poster
* Genre
* Release Year
* Rating
* Synopsis
* Full names of 3 cast members
* Full name of Director
* Full name of Producer
* Full name of Writer
* 3 reviews
* Titles for 3 similar movies
** Form inputs include:
** Add to user watch list
** Like or dislike
** Movie rating
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
* Getting to: Tab on top of the page that goes to user page after logging in
* Leaving: Movie links that goes to movie page from any of the three different lists of movies
* Leaving: Tabs on the top of the page to get to other pages
### List of tests for verifying the rendering of the page
* Verify username displayed matches the same username that was used to login 
* Verify movie lists are displaying correctly at that what's shown matches list in database related to username
