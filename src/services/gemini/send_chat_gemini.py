def send_chat_gemini(message, chat, callback):
    """Sends a message to the chat session and calls the callback function with the response text.

    Args:
        message: The message to send to the chat session.
        chat: The chat session to send the message to.
        callback: The callback function to call with the response text.
    """
    stream = False
    response = chat.send_message(message, stream=stream)
    text = ''

    if stream:
        for r in response:
            text += r.text
            callback(text, 'PROGRESS')
    else:
        text = response.text

    callback(text, 'FINISH')
