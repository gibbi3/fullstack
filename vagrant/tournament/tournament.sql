-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.



DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;

CREATE TABLE players (
  id SERIAL PRIMARY KEY,
  name TEXT
);

CREATE TABLE matches (
  match_num SERIAL PRIMARY KEY,
  winner INT REFERENCES players (id),
  loser INT REFERENCES players (id)
);

CREATE VIEW wins
AS
  SELECT players.id,
         players.name,
         COUNT(matches.winner)
            AS wins FROM players
         LEFT JOIN matches
                ON players.id = matches.winner
          GROUP BY players.id;

CREATE VIEW total_matches
AS
  SELECT players.id,
         players.name,
         COUNT(matches.winner)
            AS total_matches FROM players
         LEFT JOIN matches
              ON players.id = matches.winner
              OR players.id = matches.loser
        GROUP BY players.id;

CREATE VIEW player_record
AS
  SELECT players.id,
         players.name,
         wins.wins as wins,
         total_matches.total_matches as matches
         FROM players, wins, total_matches
         WHERE players.id = wins.id and  players.id = total_matches.id;
