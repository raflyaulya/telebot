import telebot 
from dotenv import * 
import os 

load_dotenv(find_dotenv()) 

TELEGRAM_API = os.getenv("TELEGRAM_API") 

if not TELEGRAM_API: 
    raise ValueError('Oops... There\'s something wrong with your TELEGRAM_API token!\nPlease, check it again.')

bot = telebot.TeleBot(TELEGRAM_API, parse_mode='HTML')

