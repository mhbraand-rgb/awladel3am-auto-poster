from telethon import events

def register_handlers(client):

    @client.on(events.NewMessage(chats=None))
    async def new_message_handler(event):

        # تجاهل الرسائل التي ليست من القناة المصدر
        if event.chat.username != "masherelwafy":
            return

        print("=" * 50)
        print("📩 منشور جديد")
        print("=" * 50)

        print("Message ID :", event.id)

        if event.message.message:
            print(event.message.message)

        if event.photo:
            print("📷 يحتوي على صورة")

        if event.video:
            print("🎥 يحتوي على فيديو")

        if event.grouped_id:
            print("🖼 ألبوم رقم:", event.grouped_id)
