import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
import os

#print("GROQ_API_KEY:", os.getenv("GROQ_API_KEY"))
client = Groq(
    api_key="gsk_your _actual_groq_api_key"
)

MODEL_NAME = "llama-3.1-8b-instant"


def extract_interaction(text: str):
    prompt = f"""
You are an AI assistant for a Pharmaceutical CRM.

Extract the following fields from the conversation.

Return ONLY valid JSON.

Fields:
- hcp_id
- hcp_name
- interaction_type
- topics_discussed
- samples_distributed
- sentiment
- outcome
- follow_up_date

Conversation:
{text}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user","content": prompt}],
        temperature=0
    )

    response_text = response.choices[0].message.content.strip()

    if response_text.startswith("```"):
        response_text = (
            response_text.replace("```json", "")
            .replace("```", "")
            .strip()
        )

    return json.loads(response_text)