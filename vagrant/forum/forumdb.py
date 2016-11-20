#
# Database access functions for the web forum.
#

import time
import bleach
import psycopg2


## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    DB = psycopg2.connect("dbname=forum")
    c = DB.cursor()
    c.execute("SELECT * from posts order by time")
    posts = ({'content': str(row[0]), 'time': str(row[1])}
            for row in c.fetchall())
    DB.close()
    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    DB = psycopg2.connect("dbname=forum")
    c = DB.cursor()
    content = bleach.clean(content, strip=True).strip()
    c.execute("INSERT INTO posts (content) values (%s)", (content,))
    DB.commit()
    DB.close()
