from state import CollegeState
from utils.llm import get_llm_response

def intent_classifier(state: CollegeState):

    prompt = """
You are an Intent Classifier.

Classify the user's query into ONLY one of these intents:

1. admission
2. exam
3. fees
4. scholarship

Return ONLY one word:
admission
exam
fees
scholarship

Do not explain anything.
"""

    intent = get_llm_response(
        state["query"],
        system_prompt=prompt
    )

    intent = intent.strip().lower()

    if "admission" in intent:
        state["intent"] = "admission"
    elif "exam" in intent:
        state["intent"] = "exam"
    elif "fees" in intent or "fee" in intent:
        state["intent"] = "fees"
    elif "scholarship" in intent:
        state["intent"] = "scholarship"
    else:
        state["intent"] = "admission"

    return state














# Project Created by Ganesh Kumar Mahto , Date: 11-07-2026, Branch: CSE-2 , Registration No: 24040445012
# Collage: Dumka Engineering College, Dumka, Jharkhand, India 