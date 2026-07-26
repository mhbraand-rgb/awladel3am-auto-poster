import asyncio

from telethon import TelegramClient

from config import API_ID, API_HASH, PHONE_NUMBER
from telegram_listener import register_handlers

SESSION_NAME = "awladel3am_session"


async def main():

    client = TelegramClient(
        SESSION_NAME,
        API_ID,
        API_HASH
    )

    await client.start(phone=PHONE_NUMBER)

    me = await client.get_me()

    print(f"✅ Logged in as {me.first_name}")

    register_handlers(client)

    print("👀 Waiting for new posts...")

    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
