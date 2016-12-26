from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Item, User

engine = create_engine('sqlite:///stock.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create dummy user
User1 = User(name="Gil Birdsong", email="gibbirdsong@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# First Category, Books
category1 = Category(user_id=1, name="Books")

session.add(category1)
session.commit()

book1 = Item(user_id=1, name="Blood Meridian", description="A nameless vagrant wanders Mexico and the American South for blood in Cormac McCarthy's bleak, but awe-inspiring magnum opus.",
                     price="$15.50", picture="http://ecx.images-amazon.com/images/I/518aJh03fdL.jpg", category=category1)

session.add(book1)
session.commit()


book2 = Item(user_id=1, name="Moby Dick", description="A mad captain's quest for revenge dooms an entire whaling ship.",
                     price="$15.50", picture="http://i.dailymail.co.uk/i/pix/2011/06/15/article-2003632-0C90802A00000578-22_233x351.jpg", category=category1)

session.add(book2)
session.commit()


# 2nd Category, Albums
category2 = Category(user_id=1, name="Albums")

session.add(category2)
session.commit()


item1 = Item(user_id=1, name="A Sailor's Guide to Earth", description="Sturgill Simpson's Grammy-nominated album.",
                     price="$10.99", picture="http://cdn3.pitchfork.com/albums/23092/homepage_large.9dd278d7.jpg", category=category2)

session.add(item1)
session.commit()



print "Created initial user, ategories, and items!"
