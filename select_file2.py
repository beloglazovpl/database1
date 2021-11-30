import sqlalchemy


URL = 'postgresql://user1:********@localhost:5432/database1'
engine = sqlalchemy.create_engine(URL)
connection = engine.connect()

# 1 - количество исполнителей в каждом жанре
connection.execute("""
SELECT genre_name, COUNT(sg.singer_id) c FROM genres g
JOIN singer_genre sg ON g.id = sg.genre_id
GROUP BY g.id
ORDER BY c DESC;
""").fetchall()

# 2 - количество треков, вошедших в альбомы 2019-2020 годов
connection.execute("""
SELECT album_name, year, COUNT(track_name) track_q FROM tracks t
JOIN albums a ON t.album_id = a.id
WHERE a.year BETWEEN 2019 and 2020
GROUP BY a.id
ORDER BY track_q DESC;
""").fetchall()

# 3 - средняя продолжительность треков по каждому альбому
connection.execute("""
SELECT album_name, AVG(t.duration) dur FROM albums a
JOIN tracks t ON a.id = t.album_id
GROUP BY a.id
ORDER BY dur DESC;
""").fetchall()

# 4 - все исполнители, которые не выпустили альбомы в 2020 году
connection.execute("""
SELECT singer_name FROM singers
WHERE singer_name != (
    SELECT singer_name FROM singers
    JOIN singer_album sa ON singers.id = sa.singer_id
    JOIN albums a ON sa.album_id = a.id
    WHERE a.year BETWEEN 2008 AND 2008
    GROUP BY singers.id)
GROUP BY singers.id;
""").fetchall()

# 5 - названия сборников, в которых присутствует конкретный исполнитель (выберите сами)
connection.execute("""
SELECT collection_name, collection_year FROM collections
JOIN track_collection tc ON collections.id = tc.collection_id
JOIN tracks t ON tc.track_id = t.id
JOIN albums a ON t.album_id = a.id
JOIN singer_album sa ON a.id = sa.album_id
JOIN singers s ON sa.singer_id = s.id
WHERE singer_name = 'Nickelback'
GROUP BY collections.id;
""").fetchall()

# 6 - название альбомов, в которых присутствуют исполнители более 1 жанра
connection.execute("""
SELECT album_name, singer_name, COUNT(g.id) FROM albums a
JOIN singer_album sa ON a.id = sa.album_id
JOIN singers s ON sa.singer_id = s.id
JOIN singer_genre sg ON s.id = sg.singer_id
JOIN genres g ON sg.genre_id = g.id
GROUP BY a.id, s.id
HAVING COUNT(g.genre_name) > 1;
""").fetchall()

# 7 - наименование треков, которые не входят в сборники
connection.execute("""
SELECT track_name FROM tracks t
LEFT JOIN track_collection tc ON t.id = tc.track_id
GROUP BY t.id
HAVING COUNT(tc.collection_id) = 0;
""").fetchall()

# 8 - исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько)
connection.execute("""
SELECT singer_name, track_name, duration FROM singers s
JOIN singer_album sa ON s.id = sa.singer_id
JOIN albums a ON sa.album_id = a.id
JOIN tracks t ON a.id = t.album_id
WHERE t.duration = (
    SELECT MIN(duration) FROM tracks)
GROUP BY s.id, t.id, t.duration;
""").fetchall()

# 9 - название альбомов, содержащих наименьшее количество треков
connection.execute("""
SELECT album_name, COUNT(tracks.id) FROM albums
JOIN tracks ON albums.id = tracks.album_id
GROUP BY albums.id
HAVING COUNT(tracks.id) = (
    SELECT MIN(tracks.id) FROM tracks);
""").fetchall()
