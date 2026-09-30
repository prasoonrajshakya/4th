-- drop database sxc;
-- show databases;
-- #1
create database sxc;
use sxc;
create table if not exists Employee(
	EID int,
    FirstName varchar(15),
    LastName varchar(15),
    DeptId smallint,
    DOB date
);
desc Employee;

-- #2
alter table Employee
add column ContactNo bigint,
add column Email varchar(30),
add column Salary Decimal(10,2);
desc Employee;

-- #3
alter table Employee
drop column DOB;
desc Employee;

-- #4
create table Department (
    DID smallint NOT NULL primary key,
    DName varchar(20) NOT NULL,
    Email varchar(20) NOT NULL
);
desc Department;

-- #5
alter table Employee
add constraint PK_Employee
primary key (EID);

alter table Employee
add constraint FK_Employee_Department
foreign key (DeptID)
references Department(DID);
desc Employee;
desc Department;

-- #6
create table if not exists Customer (
    CustomerID int primary key,
    CustomerName varchar(50) not null,
    Address varchar(100),
    Phone varchar(15)
);

create table if not exists Orders (
    OrderID int primary key,
    OrderDate date not null,
    Amount decimal(10,2),
    CustomerID int not null,
    constraint FK_Orders_Customer
        foreign key (CustomerID)
        references Customer(CustomerID)
);
desc Customer;
desc Orders;
