import re
from config import PRICE_INCREMENT, PRICE_LIMIT

def modify_price(text: str) -> str:
    pattern = r"(سعر\s*الجملة\s*[:：]?\s*)(\d+)"

    def replace(match):
        price = int(match.group(2))

        if price < PRICE_LIMIT:
            price += PRICE_INCREMENT

        return f"{match.group(1)}{price}"

    return re.sub(pattern, replace, text)
