from google import genai
from decouple import config

client = genai.Client(api_key=config('GEMINI_API_KEY'))

def get_ai_answer(question_text):
    prompt = f"You are a helpful study assistant for a college student. Answer this doubt clearly and concisely:\n\n{question_text}"
    response = client.models.generate_content(
        model='gemini-flash-latest',
        contents=prompt
    )
    return response.text