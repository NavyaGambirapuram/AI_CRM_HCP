from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import os
import json
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile",
)


class AgentState(TypedDict):
    text: str
    result: dict


def extract_data(state: AgentState):

    prompt = f"""
You are an AI assistant for a Pharmaceutical CRM.

Extract ONLY valid JSON.

Fields:

hcp_id
hcp_name
interaction_type
interaction_date
interaction_time
attendees
topics_discussed
samples_distributed
sentiment
outcome
follow_up_date

Conversation:

{state["text"]}
"""

    response = llm.invoke(
        [HumanMessage(content=prompt)]
    )

    content = response.content

    if content.startswith("```"):
        content = (
            content.replace("```json", "")
            .replace("```", "")
            .strip()
        )

    return {
        "result": json.loads(content)
    }


builder = StateGraph(AgentState)

builder.add_node("extract", extract_data)

builder.set_entry_point("extract")

builder.add_edge("extract", END)

graph = builder.compile()