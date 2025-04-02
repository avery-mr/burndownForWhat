# SQL Testing / Design


## Tables


### Users
**Description:** Stores user account and profile details  
**Fields:**  
- 'user_id'(INT, PRIMARY KEY, AUTO_INCREMENT): Unique user id
- 'username' (VARCHAR): Display name
- 'email' (VARCHAR): User email address
- 'height' (INT): User height
- 'weight' (INT): User weight
- 'location' (VARCHAR): User's home location
- 'experience_level' (INT): User's experence level 
- 'profile_pic': (TEXT): URL of user profile photo
- 'bio' (TEXT)  

**Tests:**
  - Insert a valid user and retrieve by ID
  - Make sure user_id auto-increments properly
  - Prevent duplicate usernames / emails?
  - Make sure required fields are provided
  - Update fields?
  - Delete user?

### Buddy Requests
**Description:** Holds current and past requests   
**Fields:**
- 'request_id' (INT, PRIMARY KEY)
- 'user_id' (INT, FOREIGN KEY)
- 'date' (DATE)
- 'Location' (VARCHAR)
- 'type' (VARCHAR): type (style) of climb?
- 'status' (VARCHAR)    e.g. 'open', 'matched', 'declined', etc

### Messages  
**Description:** chat or message history between buddies  
**Fields:**
- MessageID INT PRIMARY KEY AUTO_INCREMENT
- SenderID INT NON NULL
- ReceiverID INT NON NULL
- Text TEXT NON NULL
- DateTime DATETIME NON NULL

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

### The Crag  
**Description:** Forum style posts or feed style posts on 'the Crag' page (stories, pics, etc)  
**Fields:**
- 'post_id' (INT, PRIMARY-KEY)
- 'user_id' (INT, *from users(user_id)*)
- 'title' (VARCHAR)
- 'story' (TEXT)
- 'photo_url' (TEXT)
- 'location' (VARCHAR)
- 'date' (date/time?),

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
