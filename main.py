import asyncio

from app.telegram.client import client
from config.settings import PHONE_NUMBER

async def main():

    print("🚀 بدء تشغيل AwladEl3am Auto Poster")

    await client.start(phone=PHONE_NUMBER)

    me = await client.get_me()

    print(f"✅ تم تسجيل الدخول: {me.first_name}")
    print(f"🆔 {me.id}")

    dialogs = await client.get_dialogs()

    print("\n📋 القنوات الموجودة:\n")

    for dialog in dialogs:
        if dialog.is_channel:
            print(dialog.name)

    print("\n✅ الاتصال ناجح")

    await client.disconnect()

asyncio.run(main())
