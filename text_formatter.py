from config import OFFICE_NAME, WHATSAPP, SHIPPING_TEXT

def add_signature(text: str) -> str:
    signature = f"""

━━━━━━━━━━━━━━

🏢 {OFFICE_NAME}

📲 لطلب أوردر أو الاستفسار التواصل واتساب على رقم:

{WHATSAPP}

🚚 {SHIPPING_TEXT}
"""

    return text.strip() + signature
