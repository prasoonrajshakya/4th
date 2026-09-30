-- create database
create database if not exists gill_art_gallery;
use gill_art_gallery;

-- 1. create customer table
create table customer (
    customer_id int auto_increment primary key,
    customer_name varchar(100) not null,
    phone varchar(20) not null,
    street varchar(100) not null,
    city varchar(50) not null,
    state varchar(50) not null,
    postal_code varchar(20) not null
);

-- 2. create artist table
create table artist (
    artist_id int primary key,
    artist_name varchar(100) not null
);

-- 3. create painting table
create table painting (
    painting_id int auto_increment primary key,
    title varchar(150) not null,
    artist_id int not null,
    foreign key (artist_id) references artist(artist_id)
        on update cascade on delete restrict
);

-- 4. create customer_purchase table
create table customer_purchase (
    purchase_id int auto_increment primary key,
    customer_id int not null,
    painting_id int not null,
    purchase_date date not null,
    sales_price decimal(10, 2) not null,
    foreign key (customer_id) references customer(customer_id)
        on update cascade on delete cascade,
    foreign key (painting_id) references painting(painting_id)
        on update cascade on delete restrict
);

-- insert artist data
insert into artist (artist_id, artist_name)
values
(3, 'Carol Channing'),
(15, 'Dennis Frings');

-- insert customer data
insert into customer (customer_id, customer_name, phone, street, city, state, postal_code)
values
(1, 'Jackson, Elizabeth', '(555) 867-5309', '123 4th Avenue', 'Fonthill', 'ON', 'L3J 4S4');

-- insert painting data
insert into painting (painting_id, title, artist_id)
values
(101, 'Laugh with Teeth', 3),
(102, 'South toward Emerald Sea', 15),
(103, 'At the Movies', 3);

-- insert customer purchase data
insert into customer_purchase (customer_id, painting_id, purchase_date, sales_price)
values
(1, 101, '2000-09-17', 7000.00),
(1, 102, '2000-05-11', 1800.00),
(1, 103, '2002-02-14', 5550.00),
(1, 102, '2003-07-15', 2200.00);

desc customer;
desc painting;
desc artist;
desc customer_purchase;