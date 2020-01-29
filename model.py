from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
   __tablename__ = 'users'
   ID = Column(Integer, primary_key=True)
   username = Column(String)
   email = Column(String)
   password = Column(String)
   picture = Column(String)

class MoodBoard(Base):
    __tablename__ = 'MoodBoard'
    ID = Column(Integer, primary_key = True)
    postID = Column(Integer)
    
class Post(Base):
    __tablename__ = 'post'
    ID = Column(Integer, primary_key = True)
    category = Column(String)
    picture = Column(String)
    description = Column(String)


