import os
from pathlib import Path
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv(Path(__file__).resolve().parent.parent / ".env")


def get_llm_response(message: str, system_prompt: str = None) -> str:
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY not found. Please configure it in Streamlit Secrets or .env"
        )

    llm = ChatGroq(
        api_key=api_key,
        model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
        temperature=0,
    )

    messages = []

    if system_prompt:
        messages.append(SystemMessage(content=system_prompt))

    messages.append(HumanMessage(content=message))

    response = llm.invoke(messages)

    return response.content.strip()