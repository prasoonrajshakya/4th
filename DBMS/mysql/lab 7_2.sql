create database training_institute;
use training_institute;

create table if not exists student (
	StudentID varchar(5) primary key,
    StudentName varchar(20) not null,
    Program varchar(5) not null
);

create table if not exists instructor(
	InstructorID varchar(5) primary key,
    InstructorName varchar(50) not null,
    InstructorOffice varchar(5)
);

create table if not exists textbook(
	TextbookISBN int primary key,
    TextbookTitle varchar(20) not null,
    Publisher varchar(20)
);

create table if not exists course(
	CourseID varchar(5) primary key,
    CourseName varchar(20) not null,
    InstructorID varchar(5),
    TextbookISBN int,
    
    foreign key (InstructorID)
		references instructor(InstructorID),
	
    foreign key (TextbookISBN)
		references textbook(TextbookISBN)
);

create table if not exists student_course(
	StudentID varchar(5),
    CourseID varchar(5),
    Semester varchar(10),
    Grade varchar(2),
    
	primary key(StudentID, CourseID),
    
    foreign key (StudentID)
		references student(StudentID),
        
    foreign key (CourseID)
		references course(CourseID)	
);

-- student
insert into student (StudentID, StudentName, Program)
values
('S001', 'Alice', 'BIT'),
('S002', 'Bob', 'BCS'),
('S003', 'Carol', 'BIT');

-- instructor
insert into instructor (InstructorID, InstructorName, InstructorOffice)
values
('I11', 'Dr. Sharma', 'A301'),
('I12', 'Dr. Lee', 'B201'),
('I13', 'Dr. Khan', 'C105');

-- textbook
insert into textbook (TextbookISBN, TextbookTitle, Publisher)
values
(978001, 'Database Systems', 'Pearson'),
(978002, 'Python Programming', 'McGraw Hill'),
(978003, 'Computer Networks', 'Wiley');

-- course
insert into course (CourseID, CourseName, InstructorID, TextbookISBN)
values
('CS101', 'Database', 'I11', 978001),
('CS102', 'Programming', 'I12', 978002),
('CS103', 'Networking', 'I13', 978003);

-- student_course
insert into student_course (StudentID, CourseID, Semester, Grade)
values
('S001', 'CS101', 'Spring2026', 'A'),
('S001', 'CS102', 'Spring2026', 'B'),
('S002', 'CS101', 'Spring2026', 'B+'),
('S003', 'CS101', 'Spring2026', 'A-'),
('S003', 'CS103', 'Spring2026', 'B');
