from dotenv import load_dotenv
import os

load_dotenv()

class Config():
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI") 
class SK():    
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")