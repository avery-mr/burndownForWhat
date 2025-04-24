## Final Report: Team 2 - Burndown for What?

* **Project Title:** Belay Buddy
* **Team members' names:** Eric McAfee, Mitchell Avery, Christopher Taylor, Ahmed Khan, Tiffany LaRue
* **Project tracker link:** https://drive.google.com/drive/folders/1beZIkaFKalVyTnrPjIL3pgL30ewgVrrh
* **Link to 5 minute video:** a demo for a potential customer: https://cuboulder.zoom.us/rec/share/jRfsJuTc0fpkTnPskpOIIndSL-ls8Ff0H6LU_8gnxifieEtBH9R_q_oYoWBWF14.-6T2McErhz455WYD?startTime=1745298710000 Passcode: ZFK+h8Cx
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
    * We also added an embedded Google Maps search which allows the user to see common climbing areas nearby.
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
  * **What we learned, what we'd do differently, what worked and didn't, alternatives we thought, explanation of why we made different decisions:**
      * **What we learned:** what it is like to work as a software development team with various people of different levels of experience, and how to collaborate together to come up with a final product.
      * **What we'd do differently:** perhaps plan and outline the project scope more from start to finish and establish what the milestones are for the coding part of the project (get started earlier).
      * **What worked:** in the initial stages we used Trello for our project, which was very effective. We should continue using this as a project management tool in the future.
      * **What didn't work:** using outlook for communication was very ineffective, so moving to Whatsapp or a group chat allowed for more collaboration.
      * **Alternatives we thought of:** some of the alternatives we thought of in terms of improvement included using Trello to allow for more ownership and manageable deadlines over the course of the project.
      * **Why we made different decisions:** perhaps due to the time crunch at the end of the project, it became difficult to use the project management tool, which in retrospect, should have been our primary resource when things got tough.
* **Our public hosting site:** https://belay-buddy.onrender.com/
