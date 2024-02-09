from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from env_loader import config
import pymysql


database = config['DATABASE']
dialet = config['DIALECT']
username = config['DB_USERNAME']
password = config['DB_PASSWORD']
port = config['DB_PORT']
address = config['DB_ADDRESS']
db_name = config['DB_NAME']

engine = create_engine(f'{database}+{dialet}://{username}:{password}@{address}:{port}/{db_name}', echo=True)


Session = sessionmaker(bind=engine)
session = Session()

