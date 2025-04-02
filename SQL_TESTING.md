# SQL Testing / Design


## Tables


### Users
**Description:** Stores user account and profile details  
**Fields:**  
- 'user_id'(INT, PRIMARY KEY, AUTO_INCREMENT): Unique user id
- 'username' (VARCHAR UNIQUE NON NULL): Display name
- 'email' (VARCHAR UNIQUE NON NULL): User email address
- 'height' (INT): User height
- 'weight' (INT): User weight
- 'location' (VARCHAR NON NULL): User's home location
- 'experience' (ENUM('1', '2', '3', '4', '5') NON NULL: User's experience level (1 lowest, 5 highest)
- 'bio' (TEXT)  

**Tests:**
  - Insert a valid user and retrieve by ID
  - Make sure user_id auto-increments properly
  - Prevent duplicate usernames / emails?
  - Make sure required fields are provided
  - Update fields?
  - Delete user?

### Requests
**Description:** Holds current and past connection requests   
**Fields:**
- 'RequestID' INT PRIMARY KEY AUTO_INCREMENT
- 'SenderID' INT FOREIGN KEY References Users(user_id)
- 'ReceiverID' INT FOREIGN KEY References Users(user_id)
- 'DateTime' DATETIME NON NULL
- 'Location' VARCHAR
- 'Status' ENUM('open', 'matched', 'declined')

**Tests**
- Use case name : 
	- Verify friend request is sent from one user to another 
- Description:
	- Test Buddy Request page 
- Pre-conditions (what needs to be true about the system before the test can be applied):
        - Both users have valid Users(user_id)
- Test steps:
        1. Navigate to Buddy Request page
        2. Provide valid user name for receiver
        4. Click Send button
- Expected result:
        - User should be able to send friend request
- Actual result (when you are testing this, how can you tell it worked):
        - Friend request is sent to other user and logged in database
- Status (Pass/Fail, when this test was performed)
        - TBD
- Notes:
        - N/A
- Post-conditions (what must be true about the system when the test has completed successfully):
        - UserIDs are validated with Users table and request message successfully sent from Sender to Receiver
        - The 2 UserIDs,request message, datetime, and status details are logged in database.

### Messages  
**Description:** chat or message history between buddies  
**Fields:**
- MessageID INT PRIMARY KEY AUTO_INCREMENT
- SenderID INT NON NULL
- ReceiverID INT NON NULL
- Text TEXT NON NULL
- DateTime DATETIME NON NULL
- FOREIGN KEY SenderID REFERENCES Users(user_id)
- FOREIGN KEY ReceiverID REFERENCES Users(user_id)

**Test:**
- Use case name: 
	- Create a message on the My Buddies ("Base Camp") page
- Description:
	- Verify that submitting a message adds the message to the Messages table, with correct metadata, and displays on the page.
- Pre-conditions:
	- User needs to be on the My Buddies page
- Test steps:
	1. Navigate to My Buddies page
	2. Select a buddy
	3. Enter a message in the bar 
	4. Submit the message
- Expected result:
	- The message should appear as the latest message with the buddy.
- Actual result:
	- TBD
- Notes:
	- N/A
- Post-conditions:
	- The new message is added to the screen for the relevant buddy.
	- The new message is logged in the Messages table in the database.

### Connections  
**Description:** List of friends that user has connected with, used for easy meetup/climb requests
**Fields:**
- 'user_id' (INT FOREIGN KEY REFERENCES Users(user_id))
- 'friend_id' (INT FOREIGN KEY REFERENCES Users(user_id))
- PRIMARY KEY (user_id, friend_id)

## Table Relationships

## Database Access Methods

### Table: Users
**Access Method:** getUserProfile(user_id)
  - **Use case name:** Retrieve full user profile for valid user ID
  - **Description:** Test whether the correct profile is retrieved and displayed
  - **Pre-Conditions:** User with ID exists in the database
  - **Test steps:**
    1. Call getUserProfile() with known user_id
    2. Verify returned values against expected values
  - **Expected Result:** Full user profile including any joined data (if we decide to use any) is returned
  - **Actual result:**  Returned data matches expected structure and values
  - **Post-conditions:** no changes to database.
