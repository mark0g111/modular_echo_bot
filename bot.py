import asyncio
from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config


# The function of configuring and launching the bot
async def main() -> None:

    # Loading the config into the config variable
    config: Config = load_config()

    # Initialize the bot and dispatcher
    bot: Bot = Bot(token=config.tg_bot.token)
    dp: Dispatcher = Dispatcher()

    # Skip the accumulated updates and start polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())