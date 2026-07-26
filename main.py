import asyncio

from telegram.client import client
from config.settings import PHONE_NUMBER

async def main():

    await client.start(phone=PHONE_NUMBER)

    me = await client.get_me()

    print("=" * 50)
    print("تم تسجيل الدخول بنجاح")
    print("=" * 50)

    print(me.first_name)
    print(me.id)

    await client.run_until_disconnected()

asyncio.run(main())
