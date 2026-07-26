from telethon import TelegramClient
from config.settings import API_ID, API_HASH

SESSION_NAME = "awladel3am"

client = TelegramClient(
    SESSION_NAME,
    API_ID,
    API_HASH
)
