import os

import google.generativeai as genai


def conf_gemini() -> genai.GenerativeModel:

    generation_config = {
        'candidate_count': 1,
        'temperature': 1,
    }

    API_KEY = os.environ.get('GEMINI_API_KEY', '')
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(
        'gemini-pro', generation_config=generation_config
    )
    return model
