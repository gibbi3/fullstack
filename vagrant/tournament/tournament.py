#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        c = db.cursor()
        return db, c
    except:
        print("<Unable to connect>")


def deleteMatches():
    """Remove all the match records from the database."""
    db, c = connect()
    c.execute("DELETE FROM matches CASCADE")
    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""
    db, c = connect()
    c.execute("DELETE FROM players CASCADE")
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db, c = connect()
    c.execute("SELECT COUNT(*) FROM players")
    count = c.fetchone()[0]
    db.close()
    return count

def registerPlayer(name):
    """Adds a player to the tournament database.

    Args:
      name: the player's full name (need not be unique).
    """
    db, c = connect()
    c.execute("INSERT INTO players (name) VALUES (%s)", (name,))
    db.commit()
    db.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, c = connect()
    c.execute("SELECT id, name, wins, matches FROM player_record")
    records = c.fetchall()
    db.close()
    return records

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, c = connect()
    query = "INSERT INTO matches (winner, loser) values (%s, %s)"
    params = (winner, loser,)
    c.execute(query, params)
    db.commit()
    db.close()

def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    db, c = connect()
    c.execute("SELECT id, name FROM wins ORDER BY wins DESC")
    query = c.fetchall()
    results = []
    for x in xrange(0, len(query), 2):
        if len(query) % 2 == 0:
            match = (query[x][0],
                     query[x][1],
                     query[x+1][0],
                     query[x+1][1])
            results.append(match)
        else:
            print "This tournament requires an even number of players."
    db.close()
    return results
