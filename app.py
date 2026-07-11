import streamlit as st
from graph import build_graph

st.set_page_config(
    page_title="College Inquiry System",
    page_icon="🎓"
)

st.title("🎓 College Inquiry System")
st.write("Ask any question related to Admission, Fees, Exams or Scholarships.")

query = st.text_input("Enter your question")

if st.button("Ask"):

    if query.strip() == "":
        st.warning("Please enter a question.")
    else:
        graph = build_graph()

        result = graph.invoke({
            "query": query,
            "intent": "",
            "response": ""
        })

        st.success("Answer")

        st.write(result["response"])