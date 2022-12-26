# To-Do List
#### Video Demo:  <https://youtu.be/EIqJ4mMVqbg>
#### Description: A simple To-Do list that uses the pair module of Sqlite3 to store and complete task


### Functions

function get_user_task() | This function provides the first while loop for the user that returns the task they want to put onto the to-do list. It acts like a loop and a half and returns the users "task" to be cleared if they inputed a character in the terminal. Else, it will continually ask for the user to input a task until it reaches the third strike and the program exit due to improper usage.

function get_user_tz() | This functions ask the user for their timezone using the pytz libary for common timezones and the datetime libary to ensure that the users timezone is correct. By using the UTC time and their assigned time to switch to their timezone and format it in Year, Month, Day. Format with the time they posted in Hours, minutes, and Seconds as well as the last "%Z" being the timezone that they inputted. Else, the user will get a strike and be suggested to use the "H" for help. This will be used in the To-do-list on whenever they assigned the task with the inputted task from get_user_task()

function create_to_do_list() | The function makes the program more readable. Inside it, another function is called, create_db() that will then use the attributes inside the create_to_do_list being the task, and timezone handed from both the get functions.

function create_db() | The function attributes from create_to_do_list will then be transported to create_db() for use in the Database class to input into the Sqlite3 storage and then use db to get back all th inputted data from Sqlite3 to return to create_to_do_list to be printed onto the tabulate.

### Progression

First draft | I thought of concepts on making the to-do list more gamified to focus users on completing their task at hand and making in-store currenices to help in purchasing breaks, items, or cosmetics for their characters. Although, it was a rough idea on how I can entertain or focus users on their task. It was short lived, as I though of how to pytest customizing items or currenices as well as making an user avatar that changes depending on the item purchased. Many of which would have been out of my skill and needing the help of other individuals.

Second draft | After some review and though of my code. I didn't go for a base of TDD (Test Driven Development) with pytest and instead just fully eyeballed it and went straight to the program. This was my first mistake in coding the To-Do list and it would soon snowball into the pile of bugs and google searches that I had to do after finishing the program, just to find out that there were simpler solutions and answers to each of the problems. Learning to not work harder, but lazier.

Third Draft | After finishing the pytest and program. I thought of some new functions that could have been implemented into the program during August. But looking back at my code in December, its quite a mess. But it is what it is. The code itself hasn't changed, but some can be improvised. As the user isn't able to exit after completing or adding one task. The pytest for the database connects to the real database used by the user and not a temporaily one for pytesting purposes and to link connection with sqlite3 servers itself.

Closure | We improve and get better! I learned and am humbled from my mistakes and hope to continue down a long-lasting path of learning. Thank you CS50!

#### Flaws and responding Solutions
### 1: Pytesting
Database Pytest | Although the database is tested, it builds a connection with the original database in which inserts and declares if it has properly been inputed in the column. Building a stable connection between the user and Sqlite3, but... The task must be deleted in which can be seen from the program. One problem is that if the user has the same task as "Hey!" or "This is not a task" there task is elimated with the tested variables

Solution: The solution is basic. Use the LIMIT clause provided by the Sqlite3 DELETE statement to limit the deletion of the task from ascending order to one, so it deletes the latest variable which would be the tested one. Only thing is, there isn't a tutorial and I don't know how to do it since it keeps giving ne syntax operational errors. To save the headaches, I just left these task as they were and put task I think the user might not input.

#### Ideas that didn't make the cut

input -> (S) To skip and print the to-do list | Although, this was a original concept idea. After finishing the program and brainstorming methods to improve the to-do list. Adding the S to skip and print the overall to-do list will ruin the entire progrm as it functions.





