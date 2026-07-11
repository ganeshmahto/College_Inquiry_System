from state import CollegeState
from utils.llm import get_llm_response

def exam_agent(state: CollegeState):

    prompt = """
You are a College Examination Expert.

Answer only examination-related questions.

Include information such as:
- Semester exams
- Internal exams
- Exam schedule
- Admit card
- Result
- Revaluation

Give a clear and student-friendly answer.
"""

    response = get_llm_response(
        state["query"],
        system_prompt=prompt
    )

    state["response"] = response

    return state