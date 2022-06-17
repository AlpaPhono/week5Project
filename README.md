# week5Project
## Author - Ashley Alphonso
> BookMe web application


## Project Introduction
The objective of this project is to create and deploy a web application using the Flask micro-framework. 
The web app must support CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.

This app meets the following requirements

- Create an app in Python that utilises CRUD functionality.
- deploy front end using Flask
- Track progress using Scrum Style board
- Include use of external SQL database
- Documentation

### What is the app

The inital concept of the app was to create a website where musicians could upload their music and submit them for review to be added to music playlists and potentially recieve bookings from promoters.  The app would have to major users. The artists that would upload their music and promters that would upload their playlists or upcoming gigs. \
\
The CRUD Functionality displayed in this app are as follows 

* CREATE\
 - Add Artists\
 - Add Songs\

* READ\
 - View songs Artists have added.

* UPDATE\
 - Artists can change the name of their song after registering it

* DELETE\
- Artists are able to remove their songs from the web app.

## Application Design 
### Entity Relationship Diagram (ERD)
Coming up with a design that would showcase the different database relationships 
![Archecture sketch](https://user-images.githubusercontent.com/88076842/171422855-ca958668-93ff-4547-ac27-bd324a4a1b25.png)

The suggested sketch is a draft of what the final version of the database would look like. However, for the scope of this assignment the *Minium Usable SubseT*(MUST) is two tables that share a one to many relationship.

![artistSongERD](https://user-images.githubusercontent.com/88076842/171626661-1145f419-a98f-4c97-b98f-4ae6b9b5821d.png)

This ERD was created using the models function in workbench.

### User Stories 
These were the requirements artists using the app.

**As an Artist**
* I want to be able to register my song and attach a link so that it to be heard and I can be seen.
* I want to be able to log in and see my user profile so that I can clearly see what I have uploaded onto the site
* I want to be able to change what I have uploaded In case I have made a mistake

### Trello Kanban Board
I used Trello to create my kanban board, as it was suggested in the project brief.  I built off of the suggested template.  In future I will use the Jira board instead as it has better functionality when setting tasks into sprints.

![kanbanBoard](https://user-images.githubusercontent.com/88076842/171627633-bae70a2b-c081-4336-8519-bbdc9ac785e0.png)

### Risk Assesment
At the start of the project a risk assesment was carried out. The diagram below contains some of the possible risks that could occur during the process of creating the application. The likelihood of the risks occuring are colour coded to match levels given in a supplimented Key. Red being high risk and green being unlikely.
A section for **Mitigations** was created to seperate from things that were currently implimented to things that could be considered further along the project.

![RiskAssesment](https://user-images.githubusercontent.com/88076842/171648650-cf0a36df-4d94-4e50-91bd-9239fb85b878.png)


## Front End 

**Login Page**
The app opens up into the log in page. This page shares the same route as the '/home' route and so can be navigated to with the '/home' url suffix.  This is where a user that has already been registered can log in to view their music and update there songs.
![loginpage](https://user-images.githubusercontent.com/88076842/174333094-d124e7a8-a2b6-4fe9-

**Signup Page**
If a user hasn't already got an account then they will need to navigate to the sign up page using the '/signUp' url prefix. Here they can register there email, stagename and create a password.
Once signed up the page will automatically navigate them back to the login page where they can log in and begin to upload or edit their songs.
![signup](https://user-images.githubusercontent.com/88076842/174333791-b955c2c3-5420-4948-8649-e4547cb7ecb3.png)

**music page**
Once a user has logged in, They are able fill out a form to upload a new song as well as view which songs they have posted previously. This page has the url suffix of '/music' However unless logged in, a user cannot access this page. 
From here they have access to buttons which allow them to delete or update previous works.
![music page](https://user-images.githubusercontent.com/88076842/174335342-61ef6ec1-7290-4a06-844e-33ecf3c5693d.png)
![more music](https://user-images.githubusercontent.com/88076842/174335550-12c20dac-90ba-4a6a-9dee-f0fa8741adf8.png)
Pressing the delete button will remove the entry from the page and the database whilst the update button will redirect the user to the update page.

**update page**
Currently the user is only able to update the name of the song, eventually the user will be able to have access to editing any of the information about the song they had previously entered.
![update page](https://user-images.githubusercontent.com/88076842/174336088-abecfde7-8ac6-484b-b4f2-858ca8e7ce86.png)


## Testing and Automation
Unfortunately Due to time constraints thorough testing wasnt acomplished in this project.
Due to a misunderstanding on how the assertions work, I was unable to complete tests within the time frame.
![Testing1](https://user-images.githubusercontent.com/88076842/174337034-4bac7f32-2ec1-4657-b37b-adef6dd3149a.png)

![testin2](https://user-images.githubusercontent.com/88076842/174337096-9f4a5f5f-ed49-4db0-b879-1249a0a0d2c4.png)


## The Future

The app in its current state fufills the basic functionality of being a CRUD application. However There is much room for further development.  
Future work includes:
- deployment with a webhook to git hub to allow for continuous updates and automated testing.  
- reworked gui interface and navigationbar to allow easier movement between pages
- development into a many to many relationship with playlists and artists as initially suggested in the demo erd diagram.

## Acknowledgements 

Thank you to Earl Gray and Leon Robinson who's tuition and support leading up to this point has been invaluable. Also a big thank you to my cohort 22mayenable1 who have been a great class to work alongside.




