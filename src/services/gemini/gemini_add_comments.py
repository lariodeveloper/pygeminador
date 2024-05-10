
from src.services.gemini.send_chat_gemini import send_chat_gemini

def gemini_add_comments(code, chat, callback):
    message = f"""Act like a senior programmer. your comments and docstrings must be in pt-br. Add comments to my code and make the docstrings:

{code}
"""
    send_chat_gemini(message, chat, callback)