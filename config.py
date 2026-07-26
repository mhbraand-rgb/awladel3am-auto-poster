import os
from dotenv import load_dotenv

load_dotenv()

# Telegram API
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")

# Channels
SOURCE_CHANNEL = os.getenv("SOURCE_CHANNEL")
TARGET_CHANNEL = os.getenv("TARGET_CHANNEL")

# Price Rules
PRICE_INCREMENT = int(os.getenv("PRICE_INCREMENT"))
PRICE_LIMIT = int(os.getenv("PRICE_LIMIT"))

# Office Info
OFFICE_NAME = os.getenv("OFFICE_NAME")
WHATSAPP = os.getenv("WHATSAPP")
SHIPPING_TEXT = os.getenv("SHIPPING_TEXT")
