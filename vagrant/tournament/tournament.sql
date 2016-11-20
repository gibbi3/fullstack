-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP TABLE players CASCADE;
DROP TABLE matches CASCADE;

CREATE TABLE players(
  id SERIAL PRIMARY KEY,
  name TEXT,
  wins INTEGER,
  matches INTEGER
);

CREATE TABLE matches(
  match_num SERIAL PRIMARY KEY,
  playerone INT REFERENCES players (id),
  playertwo INT REFERENCES players (id),
  winner INT REFERENCES players (id),
  loser INT REFERENCES players (id)
)
