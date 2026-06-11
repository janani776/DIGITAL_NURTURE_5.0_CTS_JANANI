/*====================================================
  HANDS-ON 1
  TASK 1: Create Database and Tables
====================================================*/

-- Create Database
create database college_db;

-- Display Databases
show databases;

-- Select Database
use college_db;

-- Verify Current Database
select database();

/*
Expected Output:
college_db
*/

-- Create departments Table
create table departments(
    department_id int auto_increment primary key,
    dept_name varchar(100) not null,
    hod_name varchar(100),
    budget decimal(12,2)
);

/*
Expected Output:
Query OK, table created successfully
*/

-- Create students Table
create table students(
    student_id int auto_increment primary key,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    email varchar(100) unique not null,
    date_of_birth date,
    department_id int,
    enrollment_year int,
    foreign key(department_id)
    references departments(department_id)
);

/*
Expected Output:
Query OK, table created successfully
*/

-- Create courses Table
create table courses(
    course_id int auto_increment primary key,
    course_name varchar(150) not null,
    course_code varchar(20) unique,
    credits int,
    department_id int,
    foreign key(department_id)
    references departments(department_id)
);

/*
Expected Output:
Query OK, table created successfully
*/

-- Create enrollments Table
create table enrollments(
    enrollment_id int auto_increment primary key,
    student_id int,
    course_id int,
    enrollment_date date,
    grade char(2),
    foreign key(student_id)
    references students(student_id),
    foreign key(course_id)
    references courses(course_id)
);

/*
Expected Output:
Query OK, table created successfully
*/

-- Create professors Table
create table professors(
    professor_id int auto_increment primary key,
    prof_name varchar(100) not null,
    email varchar(100) unique,
    department_id int,
    salary decimal(10,2),
    foreign key(department_id)
    references departments(department_id)
);

/*
Expected Output:
Query OK, table created successfully
*/

-- Verify Tables
show tables;

/*
Expected Output:
departments
students
courses
enrollments
professors
*/

/*====================================================
  SAMPLE DATA INSERTION
====================================================*/

-- departments
insert into departments (dept_name, hod_name, budget) values
('Computer Science', 'Dr. Ramesh Kumar', 850000.00),
('Electronics', 'Dr. Priya Nair', 620000.00),
('Mechanical', 'Dr. Suresh Iyer', 540000.00),
('Civil', 'Dr. Ananya Sharma', 430000.00);

-- students
insert into students
(first_name, last_name, email, date_of_birth, department_id, enrollment_year)
values
('Arjun', 'Mehta', 'arjun.mehta@college.edu', '2003-04-12', 1, 2022),
('Priya', 'Suresh', 'priya.suresh@college.edu', '2003-07-25', 1, 2022),
('Rohan', 'Verma', 'rohan.verma@college.edu', '2002-11-08', 2, 2021),
('Sneha', 'Patel', 'sneha.patel@college.edu', '2004-01-30', 3, 2023),
('Vikram', 'Das', 'vikram.das@college.edu', '2003-09-14', 1, 2022),
('Kavya', 'Menon', 'kavya.menon@college.edu', '2002-05-17', 2, 2021),
('Aditya', 'Singh', 'aditya.singh@college.edu', '2004-03-22', 4, 2023),
('Deepika', 'Rao', 'deepika.rao@college.edu', '2003-08-09', 1, 2022);

-- courses
insert into courses
(course_name, course_code, credits, department_id)
values
('Data Structures & Algorithms', 'CS101', 4, 1),
('Database Management Systems', 'CS102', 3, 1),
('Object Oriented Programming', 'CS103', 4, 1),
('Circuit Theory', 'EC101', 3, 2),
('Thermodynamics', 'ME101', 3, 3);

-- enrollments
insert into enrollments
(student_id, course_id, enrollment_date, grade)
values
(1, 1, '2022-07-01', 'A'),
(1, 2, '2022-07-01', 'B'),
(2, 1, '2022-07-01', 'B'),
(2, 3, '2022-07-01', 'A'),
(3, 4, '2021-07-01', 'A'),
(4, 5, '2023-07-01', null),
(5, 1, '2022-07-01', 'C'),
(5, 2, '2022-07-01', 'A'),
(6, 4, '2021-07-01', 'B'),
(7, 5, '2023-07-01', null),
(8, 1, '2022-07-01', 'A'),
(8, 3, '2022-07-01', 'B');

-- professors
insert into professors
(prof_name, email, department_id, salary)
values
('Dr. Anand Krishnan', 'anand.k@college.edu', 1, 95000.00),
('Dr. Meena Pillai', 'meena.p@college.edu', 1, 88000.00),
('Dr. Sunil Rajan', 'sunil.r@college.edu', 2, 82000.00),
('Dr. Latha Gopal', 'latha.g@college.edu', 3, 79000.00),
('Dr. Kartik Bose', 'kartik.b@college.edu', 4, 76000.00);



/*====================================================
  TASK 2 : VERIFY NORMALIZATION
====================================================*/

-- 1NF Analysis:
-- All columns contain atomic values.
-- A violation would occur if multiple phone numbers were stored in one field.

-- 2NF Analysis:
-- All non-key attributes are fully dependent on the primary key.
-- In enrollments, student_id and course_id form a composite candidate key.
-- grade and enrollment_date depend on the complete student-course relationship.

-- 3NF Analysis:
-- No transitive dependencies exist.
-- Department details are stored in the departments table.
-- Storing dept_name in students would violate 3NF.

-- 3NF Analysis for Enrollments Table:
-- grade and enrollment_date depend directly on the enrollment record.
-- No non-key attribute depends on another non-key attribute.


/*====================================================
  TASK 3 : ALTER AND EXTEND THE SCHEMA
====================================================*/

-- Add phone_number column
alter table students
add phone_number varchar(15);

describe students;

-- Add max_seats column
alter table courses
add max_seats int default 60;

describe courses;

-- Add CHECK constraint
alter table enrollments
add constraint chk_grade
check (grade in ('A','B','C','D','F') or grade is null);

show create table enrollments;

-- Rename hod_name to head_of_dept
alter table departments
change hod_name head_of_dept varchar(100);

describe departments;

-- Drop phone_number column
alter table students
drop column phone_number;

describe students;

-- Verify using INFORMATION_SCHEMA
select column_name
from information_schema.columns
where table_schema='college_db'
and table_name='courses';

select column_name
from information_schema.columns
where table_schema='college_db'
and table_name='departments';








