from dotenv import load_dotenv
import os

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")

SOURCE_CHANNEL = os.getenv("SOURCE_CHANNEL")

PRICE_INCREMENT = int(os.getenv("PRICE_INCREMENT"))
PRICE_LIMIT = int(os.getenv("PRICE_LIMIT"))

OFFICE_NAME = os.getenv("OFFICE_NAME")
WHATSAPP = os.getenv("WHATSAPP")
SHIPPING_TEXT = os.getenv("SHIPPING_TEXT")
