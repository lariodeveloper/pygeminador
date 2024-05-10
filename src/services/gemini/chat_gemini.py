from google.generativeai.generative_models import ChatSession
from src.services.gemini.conf_gemini import conf_gemini

def chat_gemini() -> ChatSession:
    model = conf_gemini()
    return model.start_chat(
        history=[], 
        )