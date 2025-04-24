## Final Report: Team 2 - Burndown for What?

* **Project Title:** Belay Buddy
* **Team members' names:** Eric McAfee, Mitchell Avery, Christopher Taylor, Ahmed Khan, Tiffany LaRue
* **Project tracker link:** https://drive.google.com/drive/folders/1beZIkaFKalVyTnrPjIL3pgL30ewgVrrh
* **Link to 5 minute video (a demo for a potential customer):** https://cuboulder.zoom.us/rec/share/jRfsJuTc0fpkTnPskpOIIndSL-ls8Ff0H6LU_8gnxifieEtBH9R_q_oYoWBWF14.-6T2McErhz455WYD?startTime=1745298710000 Passcode: ZFK+h8Cx
* **Version control repository link:** https://github.com/avery-mr/burndownForWhat
* **Final Status Report and reflection for**
  * **What we completed:**
    * We successfully delivered a functional MVP that meets the core objective of our project: to create a web-based platform where climbers can connect, coordinate 
     events, and share their passion for climbing. The application includes low-fidelity login functionality, allowing users to log in and maintain their session 
     across multiple pages.
    * Through session tracking, we implemented key features that interact with our database using both GET and POST requests. These features include:
      * Editing and displaying basic user profile information.
      * Creating and viewing climbing events.
      * Sending and viewing previously sent messages.
    * We also added an embedded Google Maps search which allows the user to see climbing areas nearby.
    * This MVP lays the groundwork for a more refined version of the app with expanded functionality and improved user experience in future iterations. 
  * **What we were in the middle of implementing:**
    * One key feature that remains incomplete is the ability for users to "join" an event, which is essential to fulfilling the minimum use case for the events functionality. Implementing this feature requires additional backend logic to insert data into a user-event join table, introducing a level of complexity 
      beyond the basic features completed so far. Additionally, we plan to expand the events feature by introducing search functionality. This would enable users to 
      filter and discover climbing meetups based on criteria such as skill level, location, and climbing discipline, significantly enhancing the platform’s 
      usability and relevance.
  * **What we had planned for the future:**
    * In addition to completing the events functionality outlined above, we have identified several goals that would be well-suited for upcoming development sprints. These include:
      * Implementing live messaging functionality
        * While technically feasible, we determined early on that real-time messaging would introduce a new layer of complexity and significantly broaden the project’s scope.
      * Enhancing login security.
      * Developing a gear exchange or marketplace page
        * This feature would allow users to buy, sell, or trade climbing gear within the community.
      * Creating a "Crag Wall" forum page
        * Envisioned as a community-driven forum, this would give users a space to share tips, trip reports, and general climbing discussions.
      * Adding more detailed fields across all pages
      *   We plan to expand the depth and usability of each feature by incorporating additional data fields and UI improvements.
  * **Any known problems (bugs, issues):**
      * Profile does not update with list of buddies/connections and current events once you add a new connection or enroll in a new event
      * On the events page, under open events, the "join event" buttons are currently not functional
  * **Additional Reflections:**
      * **What we learned:** We learned what it is like to work as a software development team with various people of different levels of experience, and how to collaborate together to come up with a final product. We also learned he importance of adding code comments, and usage information to a project for other users. And the importance of planning early, and putting time into work breakdown, estimation, and assigning work to team members.
      * **What we'd do differently:** We would plan and outline the project scope more from start to finish and establish what the milestones are for the coding part of the project (get started earlier).
      * **What worked:** In the initial stages we used Trello for our project, which was very effective. We should continue using this as a project management tool in the future.
      * **What didn't work:** Using Outlook for communication was very ineffective, so moving to Whatsapp or a group chat allowed for more collaboration.
      * **Alternatives we thought of:** Some of the alternatives we thought of in terms of improvement included using Trello to allow for more ownership and manageable deadlines over the course of the project.
      * **Why we made different decisions:** We chose the Belay Buddy idea because it was a good combination of the ideas many of us had, and the climbing concept seemed like a fun one. Our communications (using Outlook) grew organically, as the minutes were sent over email and then much of our follow up conversations during the week would be a reply-all. Once we got toward the end of the project, we realized we needed a better tool to make communications easier. Project management happended a lot over Outlook and Google docs, and since development seemed so far away (as we were still learning needed skills in the course) Trello was put on the back burner. Many decisions around our final product development were due to the time crunch at the end of the project. It became difficult to use the project management tool, which in retrospect, should have been our primary resource when things got tough. Our decisions around which technical tools to use were about keeping things simple and trying to master the technologies we were taught in the course. 
* **Our public hosting site:** https://belay-buddy.onrender.com/
