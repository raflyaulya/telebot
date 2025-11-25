import os 
from dotenv import * 

load_dotenv(find_dotenv())

TELEGRAM_API = os.getenv('TELEGRAM_API')
BASE_URL = os.getenv('BASE_URL')