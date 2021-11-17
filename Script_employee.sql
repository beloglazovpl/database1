create table if not exists name(
	id serial primary key,
	name varchar(100) not null
)

create table if not exists chief(
	id serial primary key,
	chief_name varchar(100) not null
)

create table if not exists department(
	id serial primary key,
	department_name varchar(100) not null
)

create table if not exists chief_department(
	id serial primary key,
	chief_id integer not null references chief(id),
	department_id integer not null references department(id)
)

create table if not exists employee(
	id serial primary key,
	name_id integer not null references name(id),
	chief_department_id integer not null references chief_department(id)
)
