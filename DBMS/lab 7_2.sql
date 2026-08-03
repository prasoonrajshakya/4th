create database training_institute;
use training_institute;

create table if not exists student (
	StudentID varchar(5) primary key,
    StudentName varchar(20),
    Program varchar(5)
);

create table if not exists course(
	CourseID varchar(5) primary key,
    CourseName varchar(20)
);

create table if not exists student_course(
	StudentID varchar(5),
    CourseID varchar(5),
    
	primary key(CourseID, StudentID),
    foreign key (StudentID)
		references student(StudentID),
        
    foreign key (CourseID)
		references course(CourseID)	
);