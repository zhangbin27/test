from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DB_CONNECT_STRING = 'mysql+mysqldb://root:zhangbin@localhost/test'
engine = create_engine(DB_CONNECT_STRING,echo=True)
DB_Session = sessionmaker(bind=engine)
session = DB_Session()

from sqlalchemy import Column
from sqlalchemy.types import CHAR,Integer,String
from sqlalchemy.ext.declarative import declarative_base
BaseModel = declarative_base()

class User(BaseModel):
    __tablename__ = 'user'

    id = Column(Integer,primary_key=True)
    name = Column(CHAR(30))



query = session.query(User)
for user in query:
    print 'hello {0}'.format(user.name)
