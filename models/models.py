from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime


class OnegaiContent(Base):
    __tablename__ = 'onegaicontents'
    id = Column(Integer, primary_key=True)
    title = Column(String(128), unique=True)
    body = Column(Text)
    date = Column(DateTime, default=datetime.now())
    picture=Column(Text)
    #写真保存用のカラムを用意

    def __init__(self, title=None, body=None, date=None,picture=None):
        self.title = title
        self.body = body
        self.date = date
        self.picture=picture
        #写真用＝写真の保存名を入れる

    def __repr__(self):
        return '<Title %r>' % (self.title)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(128), unique=True)
    hashed_password = Column(String(128))

    def __init__(self, user_name=None, hashed_password=None):
        self.user_name = user_name
        self.hashed_password = hashed_password

    def __repr__(self):
        return '<Name %r>' % (self.user_name)