from time import sleep
from pyrogram import Client, filters, types
from PIL import Image
import re
import asyncio

app = Client('session', api_id='29485755', api_hash='69ad4ad665440835b2c916a9ad9a6818')


chat_id = "@anonkarubot"  #тут свой чат в котором спамить

@app.on_message(chat_id)
async def spam(client: Client, message: types.Message):
    if '/stop - завершить диалог' in message.text:  # Меняем это значение если хотим спамить в другом чате
        sleep(1.8)
        await app.send_message(chat_id, "Дароу, заебал, чё как жизнь?")
        sleep(2)
        await app.send_message(chat_id, """Ну заебись, что заебись.\n
Зацени, бро, я с кентом вейпшоп открыл vape_shop123_BOT\n
В подарок к первому заказу отсылают одноразку или жижу на выбор!)""")

        if '/stop - завершить диалог' in message.text:
             sleep(1.7)
             await app.send_sticker(chat_id, "CAACAgIAAxkBAAEH4bJj-KAOgflfOVfI0gPVPwNIwTi2WAACgiQAAlh_yUuGunKPE1k7OS4E")
             sleep(2)

             if "/stop - завершить диалог"  in message.text:  # Меняем это значение если хотим спамить в другом чате
                 await app.send_message(chat_id, "/stop")
                 sleep(1.5 )
                 await app.send_message(chat_id, "Найти собеседника 🔎")


app.run()