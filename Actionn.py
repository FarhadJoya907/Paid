
from pyrogram import Client, filters
from pyrogram.types import Message
import random
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(_name_)


api_id = 24264145  # 🛠 API ID خود را اینجا قرار دهید
api_hash = "594f6a2852ebbb3ef1387bb7c1481ab1"  # 🛠 API Hash خود را اینجا قرار دهید
bot_token = "7349308353:AAEUDycBVzP2k43pPEEZW9CbUYFyqAv-zjQ"  # 🛠 Bot Token خود را اینجا قرار دهید


app = Client("CD_907bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

reactions = ["🔥", "❤️", "💯", "🥰", "😎", "👍", "✨", "🤍", "🤣", "💥", "🌟"]


@app.on_message(filters.text & (filters.group | filters.channel))
async def react_to_message(client: Client, message: Message):
    emoji = random.choice(reactions)
    try:
        await message.react(emoji)
        logger.info(f"✅ واکنش {emoji} به پیام {message.message_id} در {message.chat.title}")
    except Exception as e:
        logger.error(f"❌ خطا در واکنش به پیام {message.message_id}: {e}")


if _name_ == "_main_":
    app.run()
