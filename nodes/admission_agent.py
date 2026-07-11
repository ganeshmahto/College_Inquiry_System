from state import CollegeState
from utils.llm import get_llm_response

def admission_agent(state: CollegeState):

    prompt = """
You are a College Admission Expert.

Answer only admission-related questions.

Include information such as:
- Admission process
- Eligibility
- Required documents
- Important dates
- Courses offered

Give a clear and student-friendly answer.
"""    

    response = get_llm_response(
        state["query"],
        system_prompt=prompt
    )

    state["response"] = response

    return state









# Project Created by Ganesh Kumar Mahto , Date: 11-07-2026, Branch: CSE-2 , Registration No: 24040445012
# Collage: Dumka Engineering College, Dumka, Jharkhand, India 