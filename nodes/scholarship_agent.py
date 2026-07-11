from state import CollegeState
from utils.llm import get_llm_response


def scholarship_agent(state: CollegeState):

    prompt = """
You are a College Scholarship Expert.

Answer only scholarship-related questions.

Include information such as:
- Government scholarships
- Merit scholarships
- Eligibility criteria
- Required documents
- Application process
- Last date

Give a clear and student-friendly answer.
"""

    response = get_llm_response(
        state["query"],
        system_prompt=prompt
    )

    state["response"] = response

    return state