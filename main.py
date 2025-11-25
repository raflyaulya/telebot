from fastapi import FastAPI, Request
from dotenv import *
import os
from telebot import types
from bot.bot_instance import bot
from bot.handlers import register_handlers
from utils.config import *


# load_dotenv(find_dotenv())

# TELEGRAM_API = os.getenv("TELEGRAM_API")
# BASE_URL = os.getenv("BASE_URL")

app = FastAPI()

register_handlers(bot)

@app.get("/")
async def home():
    return {"status": "ok", "message": "Telegram bot via webhook"}

# saat server hidup → set webhook
@app.on_event("startup")
async def startup_event():
    if not BASE_URL:
        # print("ERROR: BASE_URL belum di-set")   
        print("BASE_URL is not set! please set it in .env file")   
        return
    
    webhook_url = f"{BASE_URL}/webhook"  # bagian ini udah diganti
    print("Setting webhook :", webhook_url)

    bot.remove_webhook()
    bot.set_webhook(url=webhook_url)

# endpoint dipanggil Telegram
@app.post(f"/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = types.Update.de_json(data)
    bot.process_new_updates([update])
    return {"ok": True}
