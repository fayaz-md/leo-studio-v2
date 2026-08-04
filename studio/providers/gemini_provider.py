from google import genai

from studio.config import (
    GOOGLE_API_KEY,
    TEXT_MODEL,
)


class GeminiProvider:

    def __init__(self):

        self.client = genai.Client(
            api_key=GOOGLE_API_KEY,
        )

    def generate(self, prompt):

        response = self.client.models.generate_content(
            model=TEXT_MODEL,
            contents=prompt,
        )

        return response.text