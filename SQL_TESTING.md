# SQL Testing / Design


## Tables


### Users
**Description:** Stores user account and profile details
**Fields:**  
- 'UserID' INT PRIMARY KEY AUTO_INCREMENT: Unique user id
- 'Username' VARCHAR UNIQUE NOT NULL: Display name
- 'Email' VARCHAR UNIQUE NOT NULL: User email address
- 'Height' (INT): User height
- 'Weight' (INT): User weight
- 'Location' VARCHAR NOT NULL: User's home location
- 'Experience' ENUM('1', '2', '3', '4', '5') NOT NULL: User's experience level (1 lowest, 5 highest)
- 'Bio' TEXT: User's Bio

**Tests:**
- Use case name: 
	- Insert user into Users table
- Description:
	- Verify that user data is properly inserted
- Pre-conditions:
	- User must be on the home page
- Test steps:  
	1. User fills out signup form
	2. User clicks Submit button
- Expected result:
	- User's account is created and user is auto-navigated to their User profile page
- Actual result:
	- TBD
- Notes:
	- N/A
- Post-conditions:
	- User's data is correctly inserted into the Users table, to include being assigned a UserID automatically (auto-increment)
 	- User navigated to their Profile page

______________________________________________________________________________________________________
 
- Use case name: 
	- Search/Retrieve user by Name
- Description:
	- Verify that a user can be searched and retrieved from the Users table using their username
- Pre-conditions:
	- At least one user record exists in the Users table
- Test steps:  
	1. Navigate to Requests (or My Buddies) page
 	2. User enters a username in the search field
	3. User clicks Search button
- Expected result:
	- Correct user matching search query appear in the results
- Actual result:
	- TBD
- Notes:
	- Test both exact matches and partial name matches
- Post-conditions:
	- Correct user records are retrieved and displayed to user 

______________________________________________________________________________________________________

- Use case name: 
	- Make sure UserID auto-increments properly
- Description:
	- Verify that each new user receives a unique, auto-incrementing UserID
- Pre-conditions:
	- Users table can be either empty or some user records can already exist
- Test steps:  
	1. Insert a new user into the Users table
	2. Insert another user immediately after the first
 	3. Query the Users table and check assigned UserIDs
- Expected result:
	- Each new user receives a unique UserID, which increments by 1 from the previous entry
- Actual result:
	- TBD
- Notes:
	- Ensure deleted UserIDs do not get reused
- Post-conditions:
	- Database maintains sequential unique UserID values

______________________________________________________________________________________________________

- Use case name: 
	- Prevent duplicate usernames/emails
- Description:
	- Verify that database prevents duplicate usernames and email addresses
- Pre-conditions:
	- User with a specific username/email already exists in Users table
- Test steps:  
	1. Attempt to insert a new user with same username and/or email address as existing user
- Expected result:
	- Database rejects the duplicate entry and returns an error
- Actual result:
	- TBD
- Notes:
	- Ensure database constraints (UNIQUE) are properly enforced
- Post-conditions:
	- Users table only contains unique usernames and email addresses

______________________________________________________________________________________________________

- Use case name: 
	- Make sure all required (NOT NULL) fields are provided
- Description:
	- Verify that users cannot be created if required fields are missing
- Pre-conditions:
	- Database schema has NOT NULL constraints for required fields
- Test steps:  
	1. Attempt to insert a user with missing required fields (Username, Email, Location, Experience)
- Expected result:
	- Database rejects the entry and returns an appropriate error
- Actual result:
	- TBD
- Notes:
	- Test different combinations of missing fields
- Post-conditions:
	- Only valid user entries are allowed in the Users table

______________________________________________________________________________________________________

- Use case name: 
	- Update fields
- Description:
	- Verify that user's data can be successfully updated
- Pre-conditions:
	- User exists in the Users table
- Test steps:  
	1. Locate existing user in Users table
	2. Update 1 or more fields (email, username, experience, etc.) from the Profile page
 	3. Save changes
 	4. Retrieve updated user record
- Expected result:
	- Updated fields reflect the new values
- Actual result:
	- TBD
- Notes:
	- Ensure username/email uniqueness constraints are still enforced
- Post-conditions:
	- User's data updates correctly and persists in the database
 	- User's updated data displays on their profile page 

______________________________________________________________________________________________________

- Use case name: 
	- Delete user
- Description:
	- Verify that user can be deleted from database
- Pre-conditions:
	- User exists in the Users table
- Test steps:  
	1. Locate an existing user
	2. Delete user record
 	3. Attempt to retrieve deleted user
- Expected result:
	- User record no longer present in Users table
- Actual result:
	- TBD
- Notes:
	- Ensure cascading deletes do not remove UNintended related records
- Post-conditions:
	- User's data permenently deleted from database

______________________________________________________________________________________________________

### Buddy Event Requests
**Description:** Holds current and past buddy event requests
**Fields:**
- 'RequestID' INT PRIMARY KEY AUTO_INCREMENT: Unique RequestID
- 'SenderID' INT NOT NULL: Sender's UserID
- 'ReceiverID' INT NOT NULL: Receiver's UserID
- 'DateTime' DATETIME NOT NULL: Date and Time of the event
- 'Location' VARCHAR: Location of Sender
- 'Status' ENUM('Open', 'Accepted', 'Declined'): Status of request
- FOREIGN KEY (SenderID) References Users(UserID)
- FOREIGN KEY (ReceiverID) References Users(UserID)

**Tests**
- Use case name : 
	- Verify "Find a Buddy" request is sent to the request table
- Description:
	- Test "Find a Buddy" form submission
- Pre-conditions (what needs to be true about the system before the test can be applied):
        - A valid user, and location must exist in their respective tables
- Test steps:
  1. Navigate to Find a Buddy page
  2. Fill out the appropriate fields in the embedded form (date, time, location, climbing type)
  3. Click the "Submit" Button
- Expected result:
        - User should be able to submit a populated form
- Actual result (when you are testing this, how can you tell it worked):
        - User can see their open request on the "Find a Buddy" page.
- Status (Pass/Fail, when this test was performed)
	- TBD
- Notes:
	- N/A
- Post-conditions (what must be true about the system when the test has completed successfully):
	- Requests table contains the respective data from the form submission with the status field marked "open"

______________________________________________________________________________________________________

- Use case name : 
	- Verify pending "Find a Buddy" requests are displayed to the user
- Description:
	- Test "Find a Buddy" page displays open requests for the user to review and confirm
- Pre-conditions (what needs to be true about the system before the test can be applied):
	- 2 valid users, an open "Find a Buddy" request from the second user
- Test steps:
  1. Navigate to Find a Buddy page
  2. Check for the existing open request under the "Open" section
- Expected result:
        - User should be able to see a list of open requests in date order
- Actual result (when you are testing this, how can you tell it worked):
	- TBD
- Status (Pass/Fail, when this test was performed)
	- TBD
- Notes:
	- N/A
- Post-conditions (what must be true about the system when the test has completed successfully):
	- List of open user requests displayed in date order

______________________________________________________________________________________________________

- Use case name : 
	- Test "Join a Buddy" functionality
- Description:
	- Verify "Join a Buddy" button confirms an open "Find  a Buddy" request
- Pre-conditions (what needs to be true about the system before the test can be applied):
	- 2 valid users, an open "Find a Buddy" request from the second user
- Test steps:
  1. 1st (primary user) logs in
  2. User navigates to the requests page
  3. User clicks on the open "Find a Buddy" request they would like to join under the "Open Requests" header
  4. User is prompted to confirm
  5. User confirms
  6. User is redirected to the "Find a Buddy" page
- Expected result:
        - User should be able to join a buddy
- Actual result (when you are testing this, how can you tell it worked):
	- TBD
- Status (Pass/Fail, when this test was performed)
	- TBD
- Notes:
	- N/A
- Post-conditions (what must be true about the system when the test has completed successfully):
	- The status field on the "Requests" table is changed to "Confirmed"

______________________________________________________________________________________________________

### Messages  
**Description:** chat or message history between buddies  
**Fields:**
- 'MessageID' INT PRIMARY KEY AUTO_INCREMENT: Unique MessageID
- 'SenderID' INT NOT NULL: Sender's UserID
- 'ReceiverID' INT NOT NULL: Receiver's UserID
- 'Text' TEXT NOT NULL: Message text
- 'DateTime' DATETIME NOT NULL: Date and Time when message sent
- FOREIGN KEY (SenderID) REFERENCES Users(user_id)
- FOREIGN KEY (ReceiverID) REFERENCES Users(user_id)

**Tests:**
- Use case name: 
	- Create a message on the My Buddies ("Base Camp") page
- Description:
	- Verify that submitting a message adds the message to the Messages table, with correct metadata, and displays on the page.
- Pre-conditions:
	- User needs to be on the My Buddies page
 	- Both SenderID and ReceiverID should be valid UserIDs in Users table
- Test steps:
	1. Navigate to My Buddies page
	2. Click to select a buddy
	3. Enter a message in the text box 
	4. Click Send to send the message
- Expected result:
	- The message should appear as the latest message with the buddy.
 	- The message should appear as the latest message with current user
- Actual result:
	- TBD
- Notes:
	- N/A
- Post-conditions:
	- The new message is added to the screen for the relevant buddy.
 	- The new message is added to the screen for current user
	- The new message is logged in the Messages table in the database.

______________________________________________________________________________________________________

### Connections  
**Description:** List of buddies that user has connected with, used for easy meetup/climb requests
**Fields:**
- 'UserID' INT NOT NULL: UserID for current user
- 'BuddyID' INT NOT NULL: UserID for current user's buddy
- 'Status' TEXT NOT NULL: Captures values of 'Pending' for pending connection request, and 'Confirmed' for confirmed connection
- PRIMARY KEY (UserID, BuddyID)
- FOREIGN KEY (UserID) REFERENCES Users(UserID)
- FOREIGN KEY (BuddyID) REFERENCES Users(UserID)

**Tests:**
- Use case name: 
	- Create a pending connection between two users
- Description:
	- Verify that requesting a buddy connection inserts new data into Connections table with status of 'pending'
- Pre-conditions:
	- Both UserID and BuddyID must be valid users in Users table
- Test steps: 
	1. Navigate to Connections page
	2. Send Buddy request to another user ('Receiver')
	3. Verify connection request is received and status is pending
- Expected result:
	- The Connection request should appear on the Receiver's Profile page
- Actual result:
	- TBD
- Notes:
	- N/A
- Post-conditions:
	- Requested Connection appears on Receiver's Profile page
 	- Connections Table updated with new insert of UserID and BuddyID data and status of 'pending'
	- Both users see the pending connection on their respective pages
______________________________________________________________________________________________________

- Use case name: 
	- Confirm a connection between two users
- Description:
	- Verify that Accepting a buddy request updates the related row in the Connections table with status of 'confirmed' 
- Pre-conditions:
	- Both UserID and BuddyID must be valid users in Users table
 	- Buddy request sent by Sender and received by Receiver
  	- Receiver has clicked Accept button on request
- Test steps:  Done AFTER the Requests Accept test
	1. Navigate to Connections page
	2. Verify newly accepted connection appears on page
 	3. Verify in the Connections table that the related record has updated status of 'confirmed' 
- Expected result:
	- The Connection with buddy should appear on the page
- Actual result:
	- TBD
- Notes:
	- N/A
- Post-conditions:
	- Newly accepted Connection appears on Connection page
 	- Connections Table updated with status of 'confirmed'
	- Both users see the new confirmed connection on their respective pages

______________________________________________________________________________________________________

- Use case name: 
	- Delete a connection between two users
- Description:
	- Verify that user can delete a Connection with another user
- Pre-conditions:
	- Both UserID and BuddyID must be valid users in Users table
 	- Connection between UserID and BuddyID exists on Connections table
  	- User clicks Delete/Remove button on Connections page
- Test steps:  
	1. Navigate to Connections page
	2. Select a Connection from list/table
 	3. Click Delete/Remove button
- Expected result:
	- The Connection with buddy should disappear from the page
 	- Connection between the two users should be deleted from Connections table
- Actual result:
	- TBD
- Notes:
	- N/A
- Post-conditions:
	- Newly deleted Connection disappears from Connections page
 	- Connections Table updated with new delete of UserID and BuddyID data of specific connection
	- Neither user sees the deleted connection on their respective pages

______________________________________________________________________________________________________

### Locations  
**Description:** List of locations where users can go to climb
**Fields:**
- 'LocationID' INT PRIMARY KEY: LocationID for each unique location
- 'Name' VARCHAR UNIQUE NOT NULL: Name of climbing location
- 'Type' VARCHAR NOT NULL: type of climbing location (gym, bouldering, sport, traditional, ice, mixed, etc.)
- 'AverageRating' DECIMAL(3,2) CHECK (AverageRating BETWEEN 1 AND 10): Overall average of user ratings
- 'UserRating' INT CHECK (UserRating BETWEEN 1 AND 10): User-provided ratings of the location
- 'Notes' TEXT: User-written notes about the location

**Tests:**
- Use case name: 
	- Search for a climbing Location by type
- Description:
	- Verify that user can find a Location for their desired type of climbing
- Pre-conditions:
	- User must be valid user in Users table
 	- Location must exist in Locations table
- Test steps:  
	1. Navigate to Locations page
	2. Select a Type from list
 	3. Click Search button
- Expected result:
	- Locations with desired Type should appear in the list
- Actual result:
	- TBD
- Notes:
	- N/A
- Post-conditions:
	- Locations with desired Type should appear on Locations page
 	- Search logged in database

______________________________________________________________________________________________________

- Use case name: 
	- Search for a climbing Location by name
- Description:
	- Verify that user can find a Location for climbing based on name
- Pre-conditions:
	- User must be valid user in Users table
 	- Location must exist in Locations table
- Test steps:  
	1. Navigate to Locations page
	2. Type a Name in Search bar
 	3. Click Search button
- Expected result:
	- Locations with similar names appear in the list
- Actual result:
	- TBD
- Notes:
	- N/A
- Post-conditions:
	- Locations with searched name (and similar names) should appear on Locations page
 	- Search logged in database

______________________________________________________________________________________________________
 
- Use case name: 
	- Rate a climbing Location
- Description:
	- Verify that user can give a location a rating from 1-10 (1 worst, 10 best)
- Pre-conditions:
	- User must be valid user in Users table
 	- Location must exist in Locations table
- Test steps:  
	1. Navigate to Locations page
	2. Click Name of Location to select it
 	3. Click Rate button
  	4. Choose number between 1 and 10
  	5. Click Submit
- Expected result:
	- UserRating for Location updated
 	- Location's AverageRating updated
- Actual result:
	- TBD
- Notes:
	- N/A
- Post-conditions:
	- Location's AverageRating updated in Locations table
 	- UserRating for Location stored in database

______________________________________________________________________________________________________

## Table Relationships

<img width="437" alt="image" src="https://github.com/user-attachments/assets/d38fa8b5-3ae3-4657-8508-d98cd709ea96" />

______________________________________________________________________________________________________

## Database Access Methods

### Table: Users
**Access Method:** getUserProfile(UserID)
  - **Use case name:** Retrieve full user profile for valid UserID
  - **Description:** Test whether the correct profile is retrieved and displayed
  - **Pre-Conditions:** Valid UserID exists in the database
  - **Test steps:**
    1. Call getUserProfile() with known UserID
    2. Verify returned values against expected values
  - **Expected Result:** Full user profile including any joined data (if we decide to use any) is returned
  - **Actual result:**  TBD
  - **Post-conditions:** no changes to database.

______________________________________________________________________________________________________

### Table: Buddy Event Requests
**Access Method:** import datetime, getActiveRequests(datetime.datetime.now())
- **Use case name:** Retrieve upcoming Buddy Event Requests with date in the future
- **Description:** Test whether the upcoming requests are retrieved and displayed
- **Pre-Conditions:** There are upcoming Buddy Event Requests in the database
- **Test steps:**
    1. Call getActiveRequests() with the current date/time
    2. Verify returned values against expected values
- **Expected Result:** All event requests with date/times in the future are returned
- **Actual result:**  TBD
- **Post-conditions:** no changes to database.

______________________________________________________________________________________________________

### Table: Messages
**Access Method:** getMessage(MessageID)
  - **Use case name:** Retrieve message for valid MessageID
  - **Description:** Test whether the correct message is retrieved and displayed
  - **Pre-Conditions:** Message with ID exists in the database
  - **Test steps:**
    1. Call getMessage() with known MessageID
    2. Verify returned values against expected values
  - **Expected Result:** Full Message including any joined data (if we decide to use any) is returned
  - **Actual result:**  TBD
  - **Post-conditions:** no changes to database.

______________________________________________________________________________________________________
