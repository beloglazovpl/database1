import sqlalchemy


URL = 'postgresql://user1:********@localhost:5432/database1'
engine = sqlalchemy.create_engine(URL)
connection = engine.connect()

connection.execute("""
SELECT album_name, year
FROM albums
WHERE year >= 2018;
""").fetchall()

connection.execute("""
SELECT track_name, duration
FROM tracks
ORDER BY duration DESC;
"""). fetchone()

connection.execute("""
SELECT track_name
FROM tracks
WHERE duration >= 210;
""").fetchall()

connection.execute("""
SELECT collection_name
FROM collections
WHERE collection_year BETWEEN 2018 AND 2020;
""").fetchall()

connection.execute("""
SELECT singer_name
FROM singers
WHERE singer_name NOT LIKE '%% %%';
""").fetchall()

connection.execute("""
SELECT track_name
FROM tracks
WHERE track_name iLIKE '%%my%%';
""").fetchall()
