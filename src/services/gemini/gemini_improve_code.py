from src.services.gemini.send_chat_gemini import send_chat_gemini


def gemini_improve_code(code, chat, callback):
    message = f"""Act like a senior programmer. Improve my code:

{code}
"""
    send_chat_gemini(message, chat, callback)
