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

### Climbing Styles
**Description:** List of all available climbing styles
**Fields:**
- 'style_id' (INT, PRIMARY KEY)
- 'name' (VARCHAR): e.g. 'sport, 'trad', 'ice', 'bouldering'

### User Styles Join
**Description:** Join table for users and associated styles
**Fields:**
- 'user_id' (INT, *from users(user_id)*)
- 'style_id' (INT, *from climbing_styles(style_id)*)

### Experience Level
***Descriptiion:*** Lookup table for user climbing experience level
***Fields:***
- 'level_id' (INT, PRIMARY KEY): Value from 1 to 5
- 'label' (VARCHAR): Description of level (e.g. 'Belay Slave', 'Gumby', 'Crag Rat', 'Dirt Bag', 'Send Lord')

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
- 'message_id' (INT, PRIMARY_KEY)
- 'sender_id' (INT, *from users(user_id)*)
- 'receiver_id' (INT, *from users(user_id)*)
- 'message' (TEXT)

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

