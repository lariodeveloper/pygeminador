from google.generativeai.generative_models import ChatSession

from src.services.gemini.conf_gemini import conf_gemini


def chat_gemini() -> ChatSession:
    """Creates a ChatSession object for the Gemini-Pro model.

    Returns:
        A ChatSession object.
    """
    model = conf_gemini()
    return model.start_chat(
        history=[],
    )
