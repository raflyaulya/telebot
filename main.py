# entry point 

from bot import bot as teleChatbot
import telebot
import os 
from dotenv import * 
from fastapi import FastAPI, Request
import uvicorn

from bot import bot 
from bot.handlers import register_handlers   # register all handlers: IMPORTANT!!
register_handlers(bot)

load_dotenv(find_dotenv())

TELEGRAM_API = os.getenv("TELEGRAM_API")
BASE_URL = os.getenv('BASE_URL') 

if not TELEGRAM_API:
    raise ValueError('Oops... There\'s something wrong with your TELEGRAM_API token!\nPlease, check it again.')

# ==========================================================
# FastAPI app instance STARTING POINT
app = FastAPI()

@app.get('/') 
async def root(): 
    return{'status': 'ok', 
           'message': 'Telegram bot is running via webhook!'} 


@app.on_event('startup')
def set_webhook(): 
    # dipanggil otomatis saat server (uvicorn) start 
    # kita set webhook telegram -> URL fastapi kita 
    if not BASE_URL:
        print('BASE_URL is not set! Please set it in .env file.')
        return 
    
    webhook_url = f"{BASE_URL}/webhook/{TELEGRAM_API}"
    print(f"Setting webhook to: {webhook_url}") 

    bot.remove_webhook() 
    bot.set_webhook(url=webhook_url)


@app.post(f"/webhook/{TELEGRAM_API}")
async def telegram_webhook(request: Request): 
    # endpoint yg dipanggil telegram setiap ada update 
    data = await request.json() 
    update= telebot.types.Update.de_json(data) 
    bot.process_new_updates([update]) 
    return {'ok': True}
