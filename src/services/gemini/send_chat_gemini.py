def send_chat_gemini(message, chat, callback):
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
