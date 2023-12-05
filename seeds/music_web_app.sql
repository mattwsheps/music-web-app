DROP TABLE IF EXISTS artists CASCADE;
DROP SEQUENCE IF EXISTS artists_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS artists_id_seq;
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name text,
    genre text
);

INSERT INTO artists (name, genre) VALUES ('Taylor Swift', 'Pop');
INSERT INTO artists (name, genre) VALUES ('Nigel Kennedy', 'Classical');
INSERT INTO artists (name, genre) VALUES ('AC/DC', 'Rock');
INSERT INTO artists (name, genre) VALUES ('Pixies', 'Indie');

DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title text,
    release_year int,
    artist_id int,
    constraint fk_user foreign key(artist_id)
        references artists(id)
        on delete cascade
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO albums (title, release_year, artist_id) VALUES ('Red', 2022, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Blue Note Sessions', 2006, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Back in Black', 1980, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Death to the Pixies', 1997, 4);

DROP TABLE IF EXISTS books;
DROP SEQUENCE IF EXISTS books_id_seq;

