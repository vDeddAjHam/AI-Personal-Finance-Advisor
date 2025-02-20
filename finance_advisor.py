import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_finance_advice(financial_info):
    prompt = (
        f"Based on the following financial information, provide personalized financial advice "
        f"including budgeting tips, savings strategies, and investment suggestions:\n\n{financial_info}"
    )
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert personal finance advisor."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    info = input("Enter your financial details (income, expenses, goals, etc.):\n")
    advice = get_finance_advice(info)
    print("\nPersonal Finance Advice:\n", advice)
