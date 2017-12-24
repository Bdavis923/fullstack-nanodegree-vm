from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

myFirstResturant = Restaurant(name = "Pizza Palace")
session.add(myFirstResturant)
session.commit()
print session.query(Restaurant).all()

cheesePizza = MenuItem(name = "Cheese Pizza", description = "All natural with Fresh mozzarella" , price = "$8.99", restaurant = myFirstResturant)
session.add(cheesePizza)
session.commit()
print session.query(MenuItem).all()
