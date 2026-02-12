DROP TABLE IF EXISTS albums;

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
  artist_id int
);


INSERT INTO albums (title, release_year, artist_id) VALUES ('Title 1', 1998, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Title 2', 2007, 4);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Another title', 2023, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Final title', 1956, 3);