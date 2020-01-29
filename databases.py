from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session 


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = scoped_session(sessionmaker(bind=engine,autoflush=False))


def add_user(username,email,password,picture):
    user = User(
            username=username,
            email=email,
            password = password,
            picture=picture)
    session.add(user)
    session.commit()

def add_post(category,picture,description):
    post = Post(
        category = category,
        picture=picture,
        description = description)
    session.add(post)
    session.commit()

def edit_post(ID, Description):
    Post = session.query(Post).filter_by(ID=ID).first()
    Post.description = description
    session.commit()

def delete_post(ID):
    Post = session.query(Post).filter_by(ID=ID).delete()    
    session.commit()

def save_post(postID):
    Post = MoodBoard( 
        postID = postID)
    session.add(Post)
    session.commit()

def query_posts():
    posts = session.query(Post).all()
    return posts

def query_by_category(category):
    Posts = session.query(Post).filter_by(category=category)
    return Posts

def query_users():
    users = session.query(User).all()
    return users

def query_moodboard():
    posts = session.query(MoodBoard).all()
    return posts

def deleteall():
    return session.query(Post).delete()



#add_post("pencil","",'drawing of a cat')
