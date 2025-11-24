from fastapi import FastAPI 

app = FastAPI() 

@app.get('/')
async def root(): 
    # simplest endpoint testing 
    return {'status': 'ok', 
            'message': 'actually this Telegram bot is running and already works!', 
            'note': 'just local testing endpoint in simplest way'} 
