from openai import OpenAI
from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def get_llm_response(question: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an agriculture assistant."},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content