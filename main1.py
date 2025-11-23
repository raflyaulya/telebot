# entry point 

from bot import bot as teleChatbot
import telebot
import bot.handlers  # register all handlers: IMPORTANT!!

# main function 
def main(): 
    print('bot is running right now...') 
    teleChatbot.infinity_polling()
    # teleChatbot.


if __name__ == '__main__': 
    main()