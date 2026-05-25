from google import genai

from app.utils.config import (
    GEMINI_API_KEY,
    MODEL_NAME
)


client = genai.Client(
    api_key=GEMINI_API_KEY
)


def generate_response(prompt):

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    token_usage = 0

    try:
        token_usage = (
            response.usage_metadata
            .total_token_count
        )
    except:
        pass

    return {
        "text": response.text,
        "tokens": token_usage
    }