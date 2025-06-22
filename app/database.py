from databases import Database
from dotenv import load_dotenv

import os

load_dotenv()
host_db = os.getenv("FSTR_DB_HOST")
port = os.getenv("FSTR_DB_PORT")
password = os.getenv("FSTR_DB_PASS")
login = os.getenv('FSTR_DB_LOGIN')
db_name = os.getenv('DATABASE')

DATABASE_URL = f"postgresql://{login}:{password}@{host_db}:{port}/{db_name}" 

database = Database(DATABASE_URL)