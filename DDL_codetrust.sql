#this DDL querie is used for the initial database creation and refresh of the full database
drop database Coderstrust;
create database Coderstrust;
use Coderstrust;
create table Students(
StudentID int not null,
FirstName varchar(255), 
LastName varchar(255), 
Address varchar(255), 
Email varchar(255), 
Phone varchar(255),
DesignPointsPercent varchar(255),
DMPointsPercent varchar(255),
DevPointsPercent varchar(255),
Interest varchar(255),
DesignToInterest varchar(255),
DMToInterest varchar(255),
DevToInterest varchar(255),
Primary Key (StudentID));
create table Courses(
CourseID int not null,
StudentID int not null,
CourseName varchar(255),
CourseLvl varchar(255),
Requiments varchar(255),
CourseAreasSuggested varchar(255),
CompletionBadge varchar(255),
CONSTRAINT FK_StudCourseID foreign key (StudentID)references students(StudentID));
create table Payment(
StudentID int not null,
DaysUntilRenew varchar(255),
PaymentMethod varchar(255),
CONSTRAINT FK_StudPayID foreign key (StudentID)references students(StudentID));
create table Mentors(
CourseID int not null,
FullName varchar(255),
ContactEmail varchar(255),
ContactPhone varchar(255));