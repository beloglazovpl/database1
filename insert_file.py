import sqlalchemy

URL = 'postgresql://user1:********@localhost:5432/database1'
engine = sqlalchemy.create_engine(URL)
connection = engine.connect()

connection.execute("""
INSERT INTO genres
VALUES
    (1, 'Pop'),
    (2, 'Jazz'),
    (3, 'Rock'),
    (4, 'Rap'),
    (5, 'Indy');
""")

connection.execute("""
INSERT INTO singers
VALUES
    (1, 'Eminem'),
    (2, 'Ed Patrick'),
    (3, 'Ed Shiran'),
    (4, 'Michael Jackson'),
    (5, 'Frank Sinatra'),
    (6, 'Kanye West'),
    (7, 'Nickelback'),
    (8, 'Radiohead'),
    (9, 'Scorpions');
""")

connection.execute("""
INSERT INTO singer_genre
VALUES
    (1, 1, 3),
    (2, 1, 4),
    (3, 1, 6),
    (4, 2, 5),
    (5, 3, 2),
    (6, 3, 4),
    (7, 3, 7),
    (8, 3, 8),
    (9, 4, 1),
    (10, 4, 6),
    (11, 5, 2),
    (12, 5, 8),
    (13, 3, 9);
""")

connection.execute("""
INSERT INTO albums
VALUES
    (1, 'Kamikaze', 2018),
    (2, 'Recovery', 2010),
    (3, 'Barcelona', 2019),
    (4, 'No.6 Collaborations Project', 2019),
    (5, '=', 2021),
    (6, 'Thriller', 1982),
    (7, 'My Way', 1969),
    (8, 'It Might as Well Be Swing', 1964),
    (9, 'The Life of Pablo', 2016),
    (10, 'Dark Horse', 2008),
    (11, 'All The Right Reasons', 2005),
    (12, 'OK Computer', 1997),
    (13, 'Kid A', 2000),
    (14, 'The Marshall Mathers LP', 2000),
    (15, 'Sinatra 65: The Singer Today', 1964),
    (16, 'Crazy World', 1990),
    (17, 'Kids See Ghosts', 2018);
""")

connection.execute("""
INSERT INTO tracks
VALUES
    (1, 'Venom', 269, 1),
    (2, 'Not Afraid', 250, 2),
    (3, 'Blow my cover', 166, 3),
    (4, 'Beautiful People', 197, 4),
    (5, 'Shivers', 207, 5),
    (6, 'Billie Jean', 290, 6),
    (7, 'Beat It', 258, 6),
    (8, 'My Way', 275, 7),
    (9, 'Fly Me to the Moon', 150, 8),
    (10, 'Ultralight Beam', 320, 9),
    (11, 'If Today Was Your Last Day', 248, 10),
    (12, 'Follow You Home', 260, 11),
    (13, 'Fight for All the Wrong Reasons', 223, 11),
    (14, 'No Surprises', 228, 12),
    (15, 'Everything In Its Right Place', 251, 13),
    (16, 'The Way I Am', 289, 14),
    (17, 'My Kind Of Town', 205, 15),
    (18, 'Wind of Change', 310, 16),
    (19, 'Feel the Love', 165, 17);
""")

connection.execute("""
INSERT INTO singer_album
VALUES
    (1, 1, 1),
    (2, 2, 1),
    (3, 3, 2),
    (4, 4, 3),
    (5, 5, 3),
    (6, 6, 4),
    (7, 7, 5),
    (8, 8, 5),
    (9, 9, 6),
    (10, 10, 7),
    (11, 11, 7),
    (12, 12, 8),
    (13, 13, 8),
    (14, 14, 1),
    (15, 15, 5),
    (16, 16, 9);
""")

connection.execute("""
INSERT INTO collections
VALUES
    (1, 'Greatest Hits', 2012),
    (2, 'Michael Jackson: The Ultimate Collection', 2004),
    (3, 'Curtain Call: The Hits', 2005),
    (4, 'Sinatra at the Sands', 1966),
    (5, 'Nothing But the Best (Remastered)', 2008),
    (6, 'Moment of Glory', 2000),
    (7, 'Comeblack', 2011),
    (8, 'Kids See Ghosts', 2018);
""")

connection.execute("""
INSERT INTO track_collection
VALUES
    (1, 1, 11),
    (2, 1, 12),
    (3, 2, 6),
    (4, 2, 7),
    (5, 3, 16),
    (6, 4, 17),
    (7, 5, 17),
    (8, 6, 18),
    (9, 7, 18),
    (10, 8, 19);
""")
