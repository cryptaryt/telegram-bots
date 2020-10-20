from telethon import TelegramClient, events, sync
from gtts import gTTS
# import os
# import random

api_id = 12345
api_hash = 'abcdefg'
bot_token = '123:abc'
tg_group = 'my_group'

client = TelegramClient('giveaway', api_id, api_hash)
client.start(bot_token=bot_token)

# SLAP action
@client.on(events.NewMessage(pattern='\!giveaway'))
async def handler(event):
    users = await client.get_participants(tg_group)
    sender = (await event.get_sender()).first_name
    winner = random.choice(users)

    await event.reply(' Weekly Giveaway winner is @' + winner.username)

# TTS action
"""
@client.on(events.NewMessage(pattern='\!tts (.+)'))
async def handler(event):
    filename = str(int(round(time.time() * 1000))) + '.mp3'
    text = event.pattern_match.group(1)[:50]
    tts = gTTS(text=text, lang='en')
    tts.save(filename)

    await event.reply(file=filename)
    os.remove(filename)
"""

client.run_until_disconnected()
