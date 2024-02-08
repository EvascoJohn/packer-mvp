from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


database = ""
dialet = ""
username = ""
password = ""
port = ""
url = ""
db_name = ""

engine = create_engine('mysql+pymysql://root:cAsCadE_ace_casad2002@localhost:3306/packerprototype', echo=True)

Session = sessionmaker(bind=engine)


session = Session()