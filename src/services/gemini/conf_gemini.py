import os

import google.generativeai as genai


def conf_gemini() -> genai.GenerativeModel:

    generation_config = {
        'candidate_count': 1,
        'temperature': 1,
    }

    gemini_api_key = os.environ.get('GEMINI_API_KEY', '')
    if not gemini_api_key:
        raise RuntimeError('GEMINI_API_KEY environment variable not set.')
    
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel(
        'gemini-pro', generation_config=generation_config
    )
    return model
