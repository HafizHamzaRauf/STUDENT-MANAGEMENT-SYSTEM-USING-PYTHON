create table User (
user_id int unique not null auto_increment,
username varchar (250) UNIQUE not null,
password varchar (50) not null,
Primary key (user_id)
);

create table Faculty (
faculty_id int unique not null auto_increment,
designation varchar (250)  not null,
main_subject varchar(250) ,
user_id int unique not null ,
primary key (faculty_id),
foreign key(user_id) references user(user_id)
);


create table Student(
student_id int not  null unique auto_increment,
semester int not null,
cgpa float  not null,
major varchar(20) ,
user_id int not null unique,
primary key (student_id),
foreign key (user_id) references  User(user_id)
)

