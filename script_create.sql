create table if not exists genres(
	id serial primary key,
	genre_name varchar(100) not null
)

create table if not exists singers(
	id serial primary key,
	singer_name varchar(100) not null
)

create table if not exists singer_genre(
	id serial primary key,
	genre_id integer not null references genres(id),
	singer_id integer not null references singers(id)
)

create table if not exists albums(
	id serial primary key,
	album_name varchar(100) not null,
	year integer not null check (year > 0)
)

create table if not exists singer_album(
	id serial primary key,
	album_id integer not null references albums(id),
	singer_id integer not null references singers(id)
)

create table if not exists collections(
	id serial primary key,
	collection_name varchar(100) not null,
	collection_year integer not null check (collection_year > 0)
)

create table if not exists tracks(
	id serial primary key,
	track_name varchar(100) not null,
	duration integer not null check (duration > 0),
	album_id integer references albums(id)
)

create table if not exists track_collection(
	id serial primary key,
	collection_id integer not null references collections(id),
	track_id integer not null references tracks(id)
)
