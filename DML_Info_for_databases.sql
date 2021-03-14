#this DML querie is used for providing an initial database values
insert into Students(StudentID, FirstName, LastName, Address, Email, Phone, DesignPointsPercent, DMPointsPercent, DevPointsPercent, Interest,DesignToInterest,DMToInterest,DevToInterest)
values (90253, 'Joseph', 'DDS', '5468 Morgan Alley Suite 598', 'ufDVF@outlook.com', 51851887, 33.33, 0.0, 33.33, 66.66, 50.0, 0.0, 50.0),
(99212, 'Amy', 'Simon', '09937 Luis Ramp', 'AtEJHzXHm@gmail.com', 24923081, 6.66, 26.66, 0, 33.33, 19.99, 80.01, 0.0),
(69061, 'Matthew', 'Welch', '01918 Dawn Keys', 'PhRiUEdbgPQ@outlook.com', 76754126, 13.33, 33.33, 26.66, 73.32, 18.18, 45.46, 36.36),
(92165, 'Andrew', 'Campbell', '785 Tyler Centers Apt. 964', 'GjE@outlook.com', 83653970, 33.33, 6.66, 13.33, 53.31999999999999, 62.51, 12.49, 25.0),
(33627, 'James', 'Simpson', '1954 Harper Square Suite 260', 'KfmZNvTztv@hotmail.com', 98329810, 13.33, 26.66, 26.66, 66.65, 20.0, 40.0, 40.0);
insert into Courses(CourseID, StudentID, CourseName, CourseLvl, Requiments, CourseAreasSuggested, CompletionBadge)
values (322, 90253,'SQL and Databases','University','Basic Coding 2, English 1','Design 20%, Digital Marketing 13.33%, Development 33.3%','SQL'),
(322, 99212,'SQL and Databases','University','Basic Coding 2, English 1','Design 20%, Digital Marketing 13.33%, Development 33.3%','SQL'),
(322, 69061,'SQL and Databases','University','Basic Coding 2, English 1','Design 20%, Digital Marketing 13.33%, Development 33.3%','SQL'),
(650, 69061,'Coding','Colleage','Math 2, English 1','Design 6,66%, Digital Marketing 0%, Development 33.3%','Coding'),
(650, 99212,'Coding','Colleage','Math 2, English 1','Design 6,66%, Digital Marketing 0%, Development 33.3%','Coding'),
(650, 33627,'Coding','Colleage','Math 2, English 1','Design 6,66%, Digital Marketing 0%, Development 33.3%','Coding'),
(890, 92165,'Complete Freelancing course','Colleage','English 2','Design 0%, Digital Marketing 33,3%, Development 6.6%','Freelancer'),
(890, 33627,'Complete Freelancing course','Colleage','English 2','Design 0%, Digital Marketing 33,3%, Development 6.6%','Freelancer'),
(890, 69061,'Complete Freelancing course','Colleage','English 2','Design 0%, Digital Marketing 33,3%, Development 6.6%','Freelancer');
insert into Mentors(CourseID, FullName, ContactEmail, ContactPhone)
values (322, 'Mahmud Abdul Al-Ahmed','maa@codetrust.comm','99999999'),
(650, 'Linda Stretch','LS@codetrust.comm','75893432'),
(890, 'John Harley','joha@codetrust.comm','58903245');
insert into payment(StudentID, DaysUntilRenew, PaymentMethod)
values (90253,'5','Western Union'),
(99212,'23','MasterCard'),
(69061,'20','VISA'),
(33627,'2','VISA'),
(92165,'13','MasterCard');