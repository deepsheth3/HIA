import os
from google import genai


class AIService:
    """
    AI service using Google Gemini (FREE tier).
    Uses the NEW google-genai SDK.
    """

    @staticmethod
    def analyze_report(prompt: str) -> str:
        api_key = api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            return "Error: Gemini API key not found."

        try:
            client = genai.Client(api_key=api_key)

            response = client.models.generate_content(
                model="models/gemini-2.5-flash",
                contents=prompt,
            )

            if not response or not response.text:
                return "AI returned an empty response."

            return response.text

        except Exception as e:
            return f"Gemini AI error: {str(e)}"
