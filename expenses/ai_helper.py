from google import genai
from decouple import config

client = genai.Client(api_key=config('GEMINI_API_KEY'))

def get_expense_insight(category_totals):
    summary_text = ", ".join([f"{cat}: ₹{amt:.2f}" for cat, amt in category_totals.items()])
    prompt = f"You are a friendly financial advisor for a college student. Here is their spending by category: {summary_text}. Give a short, encouraging 2-3 sentence insight about their spending pattern."
    response = client.models.generate_content(
        model='gemini-flash-latest',
        contents=prompt
    )
    return response.text