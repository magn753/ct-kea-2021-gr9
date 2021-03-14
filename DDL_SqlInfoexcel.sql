#this DQL querie is for geting the table needed for the excel-piechart visualisation, just export the data to an excel file, transpose the data and fit it into a piechart after this queri is run
select students.studentID,students.Designtointerest, students.DMtoInterest, students.Devtointerest
from students
right join payment
on students.studentID=payment.studentID;
