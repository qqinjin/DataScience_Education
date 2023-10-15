import telegram as tel
import asyncio

bot = tel.Bot(token="6106271024:AAGReA1pwnI5KyqBBwOPQbVmKqnjWDraEIY")
chat_id = 6265760382

async def send_telegram_message():
    await bot.send_message(chat_id=chat_id, text="화재발생")

asyncio.run(send_telegram_message())