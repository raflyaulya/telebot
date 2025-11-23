# from . import bot 
from bot import bot 
from utils.text_utils import to_uppercase, to_lowercase, reverse_text

# START command
@bot.message_handler(commands=['start']) 
def handle_start(message): 
    bot.reply_to(
        message, 
        ( 'Selamat datang!\n '
        'this is the first bot made by theRaf.\n'
        'Silakan gunakan perintah: \n '
        '/uppercase, \n/lowercase, \n/reverse untuk mengubah teks. \n'
        'ketik /help - lihat bantuan.')
        )
    
# HELP command
@bot.message_handler(commands=['help']) 
def handle_help(message): 
    bot.reply_to(
        message,( 
        'Perintah yang tersedia:\n'
        '1. Kirim teks biasa - aku ulangi (echo)\n'
        '2. Kirim: <code>uppercase: teks_kamu</code>  \n'
        '3. Kirim: <code>lowercase: teks_kamu</code>   \n'
        '4. kirim: <code>reverse: teks_kamu</code>   \n'
        'Ketik teks apa saja untuk melihat hasilnya.')
    ) 

# stop the bot 
@bot.message_handler(commands=['stop'])
def handle_stop(message): 
    bot.reply_to(message, 'I am stopping bow, see u next time!!') 
    bot.stop_polling()

# fallback handler for all text messages
@bot.message_handler(func=lambda message: True) 
def handle_text(message): 
    '''handler untuk semua pesan text (fallback)''' 
    
    text = message.text or ''
    lower_text = text.lower() 

    if lower_text.startswith('uppercase:'): 
        content = text.split(':', 1)[1].strip() 
        if not content: 
            bot.reply_to(message, 
                         'Teksnya mana nih?') 
            return 
        
        result = to_uppercase(content) 
        bot.reply_to(message, result)

    elif lower_text.startswith('lowercase:'): 
        content= text.split(':', 1)[1].strip() 
        if not content: 
            bot.reply_to(message, 
                         'Teksnya mana nih?') 
            return 
        
        result = to_lowercase(content) 
        bot.reply_to(message, result) 


    elif lower_text.startswith('reverse:'):
        content = text.split(':', 1)[1].strip() 
        if not content: 
            bot.reply_to(message, 
                         'Teksnya mana nih?') 
            return 
        
        result = reverse_text(content) 
        bot.reply_to(message, result)

    elif lower_text.startswith('capitalize:'):
        content = text.split(':', 1)[1].strip() 
        if not content: 
            bot.reply_to(message, 'ada teksnya??')

    else: 
        # default echo handler 
        bot.reply_to(message,
                     f"kamu barusan nulis: \n<code>{text}</code>"
                     ) 
        