import os
import telegram
import asyncio
from datetime import datetime

async def send_telegram_message(token, chat_id, text, photo=None):
    bot = telegram.Bot(token=token)
    if photo:
        await bot.send_photo(chat_id=chat_id, photo=photo, caption=text)
    else:
        await bot.send_message(chat_id=chat_id, text=text)

async def send_telegram_message_on_file_change(folder_path, token, chat_id):
    last_file_list = []
    while True:
        file_list = os.listdir(folder_path)
        current_file_list = [file_name for file_name in file_list if os.path.isfile(os.path.join(folder_path, file_name)) and file_name.endswith('.jpg')]

        new_files = set(current_file_list) - set(last_file_list)
        if new_files:
            last_file_list = current_file_list
            for file_name in new_files:
                file_path = os.path.join(folder_path, file_name)
                created_time = os.path.getctime(file_path)
                created_datetime = datetime.fromtimestamp(created_time)
                created_datetime_str = created_datetime.strftime('%Y-%m-%d %H:%M:%S')
                text = f'kitchen 에서 화재가 발생하였습니다 {created_datetime_str}'
                with open(file_path, 'rb') as f:
                    photo = f.read()
                await send_telegram_message(token, chat_id, text, photo=photo)

        await asyncio.sleep(5)

async def main():
    folder_path = 'C:/Users/jae12/Desktop/pycode/화재검출서비스/static/img'
    token = "6145735541:AAHVqP0HXMWUfuVLCp5qU8soDE-gl1WTqg0"
    chat_id = '6217857242'
    await send_telegram_message_on_file_change(folder_path, token, chat_id)

asyncio.run(main())