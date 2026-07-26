import asyncio
from telethon import TelegramClient
from config import API_ID, API_HASH, PHONE_NUMBER

SESSION_NAME = "awladel3am_session"

async def main():
    print("=" * 50)
    print("🚀 AwladEl3am Auto Poster")
    print("=" * 50)

    client = TelegramClient(
        SESSION_NAME,
        API_ID,
        API_HASH
    )

    await client.start(phone=PHONE_NUMBER)

    me = await client.get_me()

    print(f"✅ تم تسجيل الدخول بنجاح")
    print(f"👤 الاسم: {me.first_name}")

    if me.username:
        print(f"📱 Username: @{me.username}")

    print(f"🆔 ID: {me.id}")

    print("\nالبوت جاهز...")

    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
