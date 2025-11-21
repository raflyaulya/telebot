import telebot 
from dotenv import * 
import os 

load_dotenv(find_dotenv()) 

TELEGRAM_API = os.getenv("TELEGRAM_API") 

bot = telebot.TeleBot(TELEGRAM_API, parse_mode='HTML')

