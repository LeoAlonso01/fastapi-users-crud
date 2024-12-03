from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost:3306/fast-api"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
conn = engine.connect()
meta = MetaData()



