# SQL Testing / Design


## Tables


### Users
**Description:** Stores user account and profile details
**Fields:**  
- 'UserID'INT PRIMARY KEY AUTO_INCREMENT: Unique user id
- 'Username' VARCHAR UNIQUE NON NULL: Display name
- 'Email' VARCHAR UNIQUE NON NULL: User email address
- 'Height' (INT): User height
- 'Weight' (INT): User weight
- 'Location' VARCHAR NON NULL: User's home location
- 'Experience' ENUM('1', '2', '3', '4', '5') NON NULL: User's experience level (1 lowest, 5 highest)
- 'Bio' TEXT: User's Bio

**Tests:**
  - Insert a valid user and retrieve by ID
  - Make sure UserID auto-increments properly
  - Prevent duplicate usernames / emails
  - Make sure required fields are provided
  - Update fields
  - Delete user

### Requests
**Description:** Holds current and past connection requests   
**Fields:**
- 'RequestID' INT PRIMARY KEY AUTO_INCREMENT: Unique RequestID
- 'SenderID' INT NON NULL: Sender's UserID
- 'ReceiverID' INT NON NULL: Receiver's UserID
- 'DateTime' DATETIME NON NULL: Date and Time when request was sent
- 'Location' VARCHAR: Location of Sender
- 'Status' ENUM('Open', 'Accepted', 'Declined'): Status of request
- FOREIGN KEY (SenderID) References Users(UserID)
- FOREIGN KEY (ReceiverID) References Users(UserID)

**Tests**
- Use case name : 
	- Verify buddy request is sent from one user to another 
- Description:
	- Test Buddy Request page 
- Pre-conditions (what needs to be true about the system before the test can be applied):
        - Both users have valid Users(user_id)
- Test steps:
  1. Navigate to Buddy Request page
  2. Provide valid user name for receiver
  3. Click Send Button
- Expected result:
        - User should be able to send buddy request
- Actual result (when you are testing this, how can you tell it worked):
        - Buddy request is sent to other user and logged in database
- Status (Pass/Fail, when this test was performed)
        - TBD
- Notes:
        - N/A
- Post-conditions (what must be true about the system when the test has completed successfully):
	- UserIDs are validated with Users table and request message successfully sent from Sender to Receiver
 	- The 2 UserIDs,request message, datetime, and status details are logged in database.

- Use case name : 
	- Verify request status is updated when receiver accepts request
 	- Verify Connections table updated with new Connection between 2 UserIDs
- Description:
	- Test Buddy Request page status updates
- Pre-conditions (what needs to be true about the system before the test can be applied):
	- Both users have valid Users(UserID)
	- One user (Sender) has sent the other user (Receiver) a buddy request
 	- Receiver can view buddy request
- Test steps:
  1. Navigate to Buddy Request page
  2. Navigate to received request
  3. Click Accept button
- Expected result:
        - User should be able to accept buddy request
- Actual result (when you are testing this, how can you tell it worked):
	- Message sent to Sender telling them that request was Accepted
        - Buddy request is accepted and Connections table updated to include the connection
- Status (Pass/Fail, when this test was performed)
        - TBD
- Notes:
        - N/A
- Post-conditions (what must be true about the system when the test has completed successfully):
	- UserIDs are added to connections table
 	- The 2 UserIDs and status details are logged in database

- Use case name : 
	- Verify request status is updated when receiver declines request
- Description:
	- Test Buddy Request page status updates
- Pre-conditions (what needs to be true about the system before the test can be applied):
	- Both users have valid Users(UserID)
	- One user (Sender) has sent the other user (Receiver) a buddy request
 	- Receiver can view buddy request
- Test steps:
  1. Navigate to Buddy Request page
  2. Navigate to received request
  3. Click Decline button
- Expected result:
        - User should be able to decline buddy request
- Actual result (when you are testing this, how can you tell it worked):
	- Buddy request status is updated to Declined
	- Message sent to Sender that their request was declined
- Status (Pass/Fail, when this test was performed)
        - TBD
- Notes:
        - N/A
- Post-conditions (what must be true about the system when the test has completed successfully):
	- UserIDs are added to connections table
 	- The 2 UserIDs and status details are logged in database

### Messages  
**Description:** chat or message history between buddies  
**Fields:**
- MessageID INT PRIMARY KEY AUTO_INCREMENT: Unique MessageID
- SenderID INT NON NULL: Sender's UserID
- ReceiverID INT NON NULL: Receiver's UserID
- Text TEXT NON NULL: Message text
- DateTime DATETIME NON NULL: Date and Time when message sent
- FOREIGN KEY (SenderID) REFERENCES Users(user_id)
- FOREIGN KEY (ReceiverID) REFERENCES Users(user_id)

**Test:**
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

### Connections  
**Description:** List of buddies that user has connected with, used for easy meetup/climb requests
**Fields:**
- 'UserID' INT NON NULL: UserID for current user
- 'BuddyID' INT NON NULL: UserID for current user's buddy
- PRIMARY KEY (UserID, BuddyID)
- FOREIGN KEY (UserID) REFERENCES Users(UserID)
- FOREIGN KEY (BuddyID) REFERENCES Users(UserID)

## Table Relationships

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
  - **Actual result:**  Returned data matches expected structure and values
  - **Post-conditions:** no changes to database.

### Table: Messages
**Access Method:** getMessage(MessageID)
  - **Use case name:** Retrieve message for valid MessageID
  - **Description:** Test whether the correct message is retrieved and displayed
  - **Pre-Conditions:** Message with ID exists in the database
  - **Test steps:**
    1. Call getMessage() with known MessageID
    2. Verify returned values against expected values
  - **Expected Result:** Full Message including any joined data (if we decide to use any) is returned
  - **Actual result:**  Returned Message matches expected structure and values
  - **Post-conditions:** no changes to database.
