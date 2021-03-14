#import mySQL connector and faker in order to be able to run this script
import mysql.connector
import random
import faker
import string
#connecting to my local database on my server, replace host, user, password and database with your own settings
mydb = mysql.connector.connect(
host="127.0.0.1",
user="root",
password="Pepega123",
database="coderstrust"
)
#beggining on reegistration process asking for name, LastName, Adress, Email, phone number and payment method
print('Welcome to you acoount regestration!')
print('Please Enter your first name: ')
y=input()
while True:
    if y.isalpha()==True:
        break
    else:
        print('Please only use letters')
        y=input()
print('Please input your last name:')
x=input()
while True:
    if x.isalpha()==True:
        break
    else:
        print('Please only use letters')
        x=input()
print('Please enter your address: ')
z=input()
print('Please enter your EMail adress: ')
v=input()
while True:
    if '@' in v and '.' in v and (v.index('@')<v.index('.')):
        break
    else:
        print('Please enter a valid email')
        v=input()
print('Please enter your Phone Number: ')
c=input()
while True:
    if c.isnumeric()==True and len(c)==8:
        break
    else:
        print('Please enter a valid phone number of length 8')
        c=input()
print('Please register your payment method (currently accepting VISA, Mastercard, Western Union): ')
payments=['VISA','Mastercard','Western Union']
l=input()
while True:
    if l in payments:
        break
    else:
        print('Please use of the options provided')
        l=input()
k=0
g=0
o=0
p=0
i=0
f=0
n=0
#giving a raandom studentID to the newly registring user
def ID():
    return random.randint(10000, 99999)
j=ID()
#adding the users information to the database, most calculation columns are left with 0 for now
mycursor2 = mydb.cursor()
sql2='INSERT INTO Students(StudentID,FirstName,LastName,Address,Email,Phone,DesignPointsPercent,DMPointsPercent,DevPointsPercent,Interest,DesignToInterest,DMToInterest,DevToInterest) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
val2=[(j,y,x,z,v,c,'0','0','0','0','0','0','0')]
mycursor2.executemany(sql2, val2)
mydb.commit()
#inserting payment info into the payment table
mycursor3=mydb.cursor()
sql3='INSERT INTO Payment(StudentID,DaysUntilRenew,PaymentMethod) VALUES (%s,%s,%s)'
val3=[(j,'30',l)]
mycursor3.executemany(sql3, val3)
mydb.commit()
#begining on the quiz
mycursor = mydb.cursor()
print('Please answer the following questions with yes/no: ')
def question(question,sql):
    mycursor = mydb.cursor()
    print(question)
    while True:
        a=input()
        if a=='yes':
            val=[(question,'5')]
            break
        elif a=='no':
            val=[(question,'0')]
            break
        else:
            print("Please use yes/no")
    mycursor.executemany(sql, val)
    mydb.commit()
    return
#list of questions
qlist=['Do you find yourself to be creative?','Have you had experience with design before?','Do you enjoy designing visual presentations?','Do you enjoy editing?','Have you had experience with editing software beforehand?']
qlist2=['Have you had experience running a social media account?','Do you consider yourself as having a flair for SoME?','Do you find yourself contacting other people on social media?','Have you had experience with marketing?','Do you find yourself influenced by advertising on social media?']
qlist3=['Do you think more logically and methodically rather than openly and creatively?','Have you had experience with coding before?','Do you have a passion for overcoming obstacles using your analytical skills?','Are you a fast learner?','Do you have the ability to concentrate for a prolonged period of time?']
#insertion of students answers and the coresponding questions into the databes
sql='INSERT INTO DesignQuestions(Design, DesignPoints) VALUES (%s,%s)'
for i in qlist:#for loop1
    question(i,sql)
sql='INSERT INTO DMQuestions(DigitalMarketing,DMPoints) VALUES (%s,%s)'
for i in qlist2:#for loop2
    question(i,sql)
sql='INSERT INTO DevQuestions(Development,DPoints) VALUES (%s,%s)'
for i in qlist3:#for loop3
    question(i,sql)
#Sign up process for the courses and the addition of that data to the courses table, user can apply to multiple courses, but only once to each
selection=0
coursesselected=[0,0,0]
while selection!=4:
    print('Would you like to sign up to some courses? (Currently availible courses are SQL and Databases, Coding and Complete Freelancing Course)')
    print('Press 1 if you would like to sign up for SQL and Databases')
    print('Press 2 if you would like to sign up for Coding')
    print('Press 3 if you would like to sign up for Complete Freelancing Course')
    print('Press 4 if you have signed up for all the courses that you wanted to be a part of')
    selection=int(input())
    if selection==1 and coursesselected[0]==0:
        mycursor4=mydb.cursor()
        coursesselected[0]=1
        sql4='INSERT INTO Courses(CourseID,StudentID, CourseName, CourseLvl, Requiments, CourseAreasSuggested, CompletionBadge) VALUES (%s,%s,%s,%s,%s,%s,%s)'
        val4=[('322',j, 'SQL and Databases', 'University', 'Basic Coding 2, English 1', 'Design 20%, Digital Marketing 13.33%, Development 33.3%', 'SQL')]
        mycursor4.executemany(sql4, val4)
        mydb.commit()
        print('You have been Signer up for SQL and Databases')
    elif selection==2 and coursesselected[1]==0:
        mycursor5=mydb.cursor()
        coursesselected[1]=1
        sql5='INSERT INTO Courses(CourseID,StudentID, CourseName, CourseLvl, Requiments, CourseAreasSuggested, CompletionBadge) VALUES (%s,%s,%s,%s,%s,%s,%s)'
        val5=[('650',j, 'Coding', 'Colleage', 'Math 2, English 1', 'Design 6,66%, Digital Marketing 0%, Development 33.3%', 'Coding')]
        mycursor5.executemany(sql5, val5)
        mydb.commit()
        print('You have been Signer up for Coding')
    elif selection==3 and coursesselected[2]==0:
        mycursor6=mydb.cursor()
        coursesselected[2]=1
        sql6='INSERT INTO Courses(CourseID,StudentID, CourseName, CourseLvl, Requiments, CourseAreasSuggested, CompletionBadge) VALUES (%s,%s,%s,%s,%s,%s,%s)'
        val6=[('890',j,'Complete Freelancing course', 'Colleage', 'English 2', 'Design 0%, Digital Marketing 33,3%, Development 6.6%', 'Freelancer')]
        mycursor6.executemany(sql6, val6)
        mydb.commit()
        print('You have been Signer up for Complete Freelancing course')
    elif selection==1 or selection==2 or selection==3:
        print('You have already signed up for this course!')
    elif selection==4:
        print('Thank you for signing up with CodersTrust.')
        break
#en of the python script
