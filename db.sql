create database blood_db;
use blood_db;
create table Donor(id int primary key auto_increment,
       name varchar(100),
       blood_group varchar(50),
       phone varchar(15) unique,
       city varchar(100),
       last_donation date
       );
select * from donor;
alter table donor modify blood_group varchar(50);
drop table donor;
show create table donor;
select 1;
drop database blood_db;


