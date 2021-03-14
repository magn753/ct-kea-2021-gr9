This is a readme for usage of SQL and the attached python scripts.
S1. Begin by opening your local server and running the coderstrust.sql file, in order to create the coderstrust database with students, courses, payment and mentors tables.
S2. Next, run the info for databases.sql file in order to fill the newly created tables with sample information.
(If its the first time using the database, than skip using the droping quiz tables.sql, and go straight to creation of quiz tables.sql),
S3. Run droping quiz tables.sql to drop already existing information about the latest user who took the quiz.
S4. Next run the creation of quiz tables.sql in order to create blank tables for the data for the interest parameters that will be added after the quiz
At this point you will be looking at the process from the users persektive, 
S5. Switch to using python script titled sqlquiz.py (do not forget to change the settings inside the script so that you can connect to your own server) and fill in the information that it asks about (this includes first name, last name, adress, email, phone and payment information)
S6. The script will then give you the quiz that you have to answer with yes/no,
S7. The script will than ask you to choose which courses you would like to sign up for,
At this point your perspective will switch back to that of a Codertrust employee,
S8. Go back to the your server and check the newly added information in the student, courses and payment method,
S9. Next check the students table for the studentID that was given through the script,
S10. Insert the studentID into the lines 7, 12, 17, 20, 23, 26 in the sql point.sqls, in order to update the row with the selected studentID row in the students table and run the queri,
S11. Check the newly added information in the student table,
S12. Run the sqlinfoexcel.sql to have the data needed for excel pie charts selected from the students table,
S13. Export the data to an excel file and transpose it,
S14. Create a pie chart using the data in the excel file (an example on how its done can be seen in the Example on how visual look of student data.xlsx)
S15.(optional) If you want to add more students you can start the process from S3, 
S16.(optional) If you are not bothered to go through the quiz again you can use the RandomGenerato1.py to create data values for a random student and place it in the info for databases.sql query under the values that are added to the students table, remember that you will also need to insert information for the classes and payment otions based on the studentID in this case.


 _____                         _____  
|  __ \                       |  _  | 
| |  \/_ __ ___  _   _ _ __   | |_| | 
| | __| '__/ _ \| | | | '_ \  \____ | 
| |_\ \ | | (_) | |_| | |_) | .___/ / 
 \____/_|  \___/ \__,_| .__/  \____/  
                      | |             
                      |_|             