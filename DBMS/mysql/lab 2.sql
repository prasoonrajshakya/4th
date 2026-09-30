create database if not exists db;
use db;
-- drop table Employee;
-- drop table Department;

-- #1
CREATE TABLE IF NOT EXISTS Employee (
    EmpNo INT auto_increment PRIMARY KEY,
    EmpName VARCHAR(100),
    Job VARCHAR(100),
    DeptNo INT,
    Phone_no VARCHAR(20),
    YearOfEnrollment INT,
    EmailAddress VARCHAR(100),
    PostalAddress INT
);
desc Employee;

CREATE TABLE IF NOT EXISTS Department (
    DeptNo INT PRIMARY KEY,
    DeptName VARCHAR(100),
    DeptEmail VARCHAR(100),
    DeptHOD VARCHAR(100)
);

desc Department;

-- #4
INSERT INTO Department
(DeptNo, DeptName, DeptEmail, DeptHOD)
VALUES
(2, 'Computer Science', 'cs@sxc.edu.np', 'Mr. Ganesh Yogi'),
(3, 'MicroBiology', 'microbio@sxc.edu.np', 'Mrs. Pramila Parajuli'),
(4, 'Physics', 'physics@sxc.edu.np', 'Mr. Binod Bhandari'),
(5, 'Business Studies', 'bs@sxc.edu.np', 'Mr. Maha Prasad Shrestha');

select * from Department;
-- #2
ALTER TABLE Employee
ADD CONSTRAINT fk_employee_department
FOREIGN KEY (DeptNo)
REFERENCES Department(DeptNo);

-- #3
INSERT INTO Employee
(EmpName, Job, DeptNo, Phone_no, YearOfEnrollment, EmailAddress, PostalAddress)
VALUES
('Abhiyan Sainju', 'Teaching Assistant', 2, '5544332', 2016, 'abhiyansainju@gmail.com', 4066),
('Babis Shrestha', 'Software Developer', 2, '7744533', 2018, 'babis@gmail.com', 3056),
('Chetana Panta', 'Coordinator', 4, '3322551', 2015, 'chetana@gmail.com', 4066),
('Diwas Sapkota', 'Researcher', 4, '776644', 2014, 'diwas@gmail.com', 9088),
('Elina Malla', 'DBA', 3, '4433532', 2019, 'elina@gmail.com', 3056),
('Indu Adhikari', 'Counsellor', 5, '352625', 2020, 'indu@gmail.com', 5504);

select * from Employee;

-- #5
INSERT INTO Employee
(EmpName, Job, DeptNo, Phone_no, YearOfEnrollment, EmailAddress, PostalAddress)
VALUES
('Rameshwor Dhakal', 'Lab Manager', 1, '5589212', 2016, 'rameshwordhakal@gmail.com', 1234);

-- #6
select * from Employee where DeptNo = 3;

-- #7
select * from Employee where YearOfEnrollment = 2016;

-- #8
UPDATE Employee
SET Phone_no = '3344225'
WHERE EmpNo = 3;

-- #9
-- delete from Employee where DeptNo = 3;
select * from Employee;

select * from Department;

-- #10
delete from Department where DeptNo = 4;