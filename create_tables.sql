create table employee(
    id int primary key,
    name varchar(50),
    salary int,
    departmentId int
);

create table department(
    id int primary key,
    name varchar(50)
);

create table stock(
    id int primary key,
    stock_name varchar(50),
    operation enum('buy', 'sell'),
    operation_day int,
    price decimal
);


create table salesman(
    salesman_id int primary key,
    name varchar(50),
    city varchar(50),
    commission decimal
);

create table customer(
    customer_id int primary key,
    customer_name varchar(50),
    city varchar(50),
    grade int,
    salesman_id int
);

create table orders(
    ord_no int primary key,
    purch_amt decimal,
    ord_date date,
    customer_id int,
    salesman_id int
);