
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random
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
    
b=range(10)
session.execute(
User.__table__.insert(),
[{'name':`random.randint(1,100)`} for i in xrange(10)]
)

session.commit()
