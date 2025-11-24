from telebot import TeleBot
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv()) 

TELEGRAM_API = os.getenv("TELEGRAM_API")

bot = TeleBot(TELEGRAM_API, parse_mode='HTML')