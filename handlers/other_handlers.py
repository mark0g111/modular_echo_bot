from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU


# Initialize the router
router: Router = Router()

# This handler will work on any of your messages,
# except for commands "/start" and "/help"
@router.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])