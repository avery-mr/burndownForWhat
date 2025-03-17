# Web Pages Design

[Google Slides - Page Design](https://docs.google.com/presentation/d/1ncAmPZ-siARAbuOKce5822HwWyBCqII-jvZPaDD3iIg/edit?usp=sharing)

### Home/Landing
<img width="311" alt="image" src="https://github.com/user-attachments/assets/38d345de-cd40-4b2e-a3f0-a8be43862938" />

* __Description:__ 
First page after successful login.  Contains links to all other pages.  May contain climbing news, weather for user's favorite climbing area, user submtitted climbing photos.
* __Required Parameters__

* __Required Data__
  * Username
  * Carry username on to other pages
  * Logo, Go image, and username input
* __Link Destinations for Page__
  * Login action links to Profile Page
* __List of tests for verifying the rendering of the page__
  * Ensure logo and login form loads correctly
  * Username correctly logs in
  * GO links to Profile page

### Profile Page
<img width="278" alt="image" src="https://github.com/user-attachments/assets/ce0be649-a9a2-4d5f-8632-57315eaf5d3b" />

* __Description__
  * Users can create and manage their personal profiles
  * Profile fields include climbing experience, preferred climbing styles, favorite locations, and short bio
  * Basic user data/stats
    * name 
    * height
    * weight
    * climbing type
      * sport
      * sport/lead
      * trad
      * ice  
    * location
  * Experience level
  * bragging wall/acomplishments
  * favorite routes
  * routes bucket list 

* __Required Parameters__
  * User authentication?
  * Profile ID for retrieving user data.

* __Required Data__
  * Name, height, weight
  * Climbing type preference
  * Home location
  * Experience level
  * Favorite routes and bucket lists
  * Profile picture
* __Link Destinations for Page__
  * Find a Buddy
  * My Buddies
  * The Crag
* __List of tests for verifying the rendering of the page__
  * Validate correct profile data loads for user
  * Verify images display properly
  * Ensure updates save correctly
  * 
### Find a Buddy
<img width="293" alt="image" src="https://github.com/user-attachments/assets/c49bee85-2028-4922-9b65-36b5b2e44cfc" />

* __Description:__  Will host a form to collect additional data for pairing up fellow users. Form will need to gather:
  * Dates available
  * Location options
  * Specific route targets
* __Required Parameters__
  * User name or ID - used to retrieve data on another table for pending and confirmed resquest records.
* __Required Data__
  * Date range
  * Time range
  * Locations (multiple values)
  * Climbing type
* __Link Destinations for Page__
  * My Profile, Find a Buddy, The Crag, Logout
  * Submit - links to the results of other requests that "match" your submission"
    * Clicking on any pending request should also bring up this same page
* __List of tests for verifying the rendering of the page__
  * Ensure pending and confirmed requests all display
  * Enter a new request, refresh, assert this populated on the pending table
  * Visit pending request, confirm a match, assert this request moves to the confirmed requests table
  
### My Buddies / Messages
<img width="313" alt="image" src="https://github.com/user-attachments/assets/1116f95d-4b11-49d6-8d2c-97c2860b8cb8" />

* __Description:__ 
  * Displays a list of added climbing partners.
  * Allows user to track availability and maintain connections.
  * Contains conversation history with each buddy and allows new messages to be added.
* __Required Parameters__
  * Name or ID of logged in user
  * Buddy that user clicks in Buddy Seach
* __Required Data__
  * Buddies
  * Message history with each buddy
* __Link Destinations for Page__
  * My profile, buddy profiles
  * Find a Buddy
  * The Crag
  * Logout
* __List of tests for verifying the rendering of the page__
  * Buddies showing up correctly
  * All messages listed in descending order by date

### The Crag
<img width="126" alt="image" src="https://github.com/user-attachments/assets/35e4ae4e-7565-47e2-a501-ed6ca101dff9" />

* __Description:__ 
  * Page displays reviews, stories and photos of various individual's rock climbing adventures
  * Individuals will be able to share a new adventure
  * Ideally, there will be a way to filter out the posts on the page by:
    * indoor vs outdoor
    * geographical location
    * date
    * etc.
* __Required Parameters__
  * Name or ID of logged in User
* __Required Data__
  * Photos/images of climbing stories
  * Narratives/personal stories of last outing
* __Link Destinations for Page__
  * Ensure that images render correctly
  * Personal stories are correctly displayed
  * Other people are able to access the website and add their own stories to the public forum
* __List of tests for verifying the rendering of the page__
  * Ensure that the images display correctly after upload
  * Personal stories are correctly shown on the website
    * When a user uploads a new adventure, it should allow the user to input relevant information
    * Adventure should then display
    * Ensure filters, etc work
  * Anyone is able to access the website.  After logging in with valid user credentials, they are then able to add their stories to the public forum
