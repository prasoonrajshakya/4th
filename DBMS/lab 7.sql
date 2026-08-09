create database uni_research;
use uni_research;

create table faculty (
	facultyID int primary key not null,
    fullName varchar(20) not null,
    designation varchar(20),
    department varchar(20),
    officePhone varchar(20),
    email varchar(30) unique
);

create table students(
	studentID int primary key,
    stuName varchar(20),
    program varchar(20),
    year varchar(4),
    email varchar(30) unique
);


create table research_area(
	areaID int primary key not null,
	areaName varchar(20),
    description varchar(100)
);

create table research_project(
	projectID int primary key,
    areaID int not null,
    facultyID int not null,
    title varchar(100),
    startDate date,
    endDate date,
    budget decimal(10,2),
    status varchar(10),
    
    foreign key (areaID)
		references research_area(areaID),
    
    foreign key(facultyID)
		references faculty(facultyID)
);

create table student_projects(
	projectID int,
    studentID int,
	joinDate date,
    role varchar(10),
    monthlyStipend decimal(10,2),
    
    primary key(projectID, studentID, joinDate),
    
    foreign key (projectID)
		references research_project(projectID),
	
    foreign key (studentID)
		references students(studentID)
);

create table funding_agency(
	agencyID int primary key,
    name varchar(20),
    country varchar(20),
    contactPerson varchar(20),
    email varchar(30) unique
);

create table project_funding(
	agencyID int,
    projectID int,
    amountFunded decimal(10,2),
    fundingDate date not null,
    
    primary key(agencyID, projectID, fundingDate),
    
    foreign key(projectID)
		references research_project(projectID),
	
	foreign key(agencyID)
		references funding_agency(agencyID)
);

create table laboratory(
	labID int primary key,
    name varchar(20),
    building varchar(20),
    capacity int
);

create table project_lab(
	projectID int,
    labID int,
    reserveStartDate date,
    reserveEndDate date,
    
    primary key(projectID, labID, reserveStartDate, reserveEndDate),
    
    foreign key(projectID)
		references research_project(projectID),
	
    foreign key(labID)
		references laboratory(labID)
);

create table publications(
	publicationID int primary key,
    projectID int,
    title varchar(10),
    journal varchar(50),
    publicationYear year,
    DOI varchar(100) unique,
    
    foreign key (projectID)
		references research_project(projectID)
);

create table authors(
	authorID int primary key,
    name varchar(20),
    email varchar(30) unique
);

create table publication_authors(
	publicationID int,
    authorID int,
    authorOrder int not null,
    correspondingAuthor boolean not null default false,
    
    primary key(publicationID, authorID),
    
    foreign key (publicationID)
		references publications(publicationID),
        
	foreign key(authorID)
		references authors(authorID)
);

desc faculty;
desc students;
desc research_area;
desc research_project;
desc student_projects;
desc funding_agency;
desc project_funding;
desc laboratory;
desc project_lab;
desc publications;
desc authors;
desc publication_authors;