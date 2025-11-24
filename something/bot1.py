import config 
import telebot
from dotenv import * 
import os 

load_dotenv(find_dotenv())
TELEGRAM_API = os.getenv("TELEGRAM_API")

bot = telebot.TeleBot(TELEGRAM_API) 

@bot.message_handler(commands=['start'])
def send_welcome(message): 
    bot.reply_to( 
        message, 
        'Hallo, selamat datang di bot kami!. \n' 
        'ketik apa saja, nanti akan aku ulangi ke kamu!!'
    ) 

# handler untuk semua pesan teks biasa 
@bot.message_handler(func=lambda message: True) 
def echo_all(message): 
    text_user = message.text 
    reply_text = f"Hey! \nKamu barusan nulis:\n\n{text_user}" 
    bot.reply_to(message, reply_text) 


# stop the bot 
@bot.message_handler(commands=['stop']) 
def stop_bot(message): 
    bot.reply_to(message, 'Bot berhenti, terima kasih sudah menggunakan bot ini!') 
    bot.stop_polling()


print('bot is running... \nPlease wait or if u wanna escape, press CTRL + C to stop the program')
bot.infinity_polling()