# entry point 

from bot import bot as teleChatbot
import telebot
import bot.handlers  # register all handlers: IMPORTANT!!

def main(): 
    print('bot is running right now...') 
    teleChatbot.infinity_polling()


if __name__ == '__main__': 
    main()