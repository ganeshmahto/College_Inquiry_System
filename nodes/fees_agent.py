from state import CollegeState
from utils.llm import get_llm_response

def fees_agent(state: CollegeState):

    prompt = """
You are a College Fees Expert.

Answer only fees-related questions.

Include information such as:
- Tuition fees
- Hostel fees
- Examination fees
- Registration fees
- Payment methods
- Fee deadlines

Give a clear and student-friendly answer.
"""

    response = get_llm_response(
        state["query"],
        system_prompt=prompt
    )

    state["response"] = response

    return state