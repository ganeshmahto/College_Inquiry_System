import streamlit as st
from graph import build_graph

st.set_page_config(page_title="College Inquiry System")

st.title("🎓 College Inquiry System")

graph = build_graph()

query = st.text_input("Enter your question")

if st.button("Ask"):

    if query.strip():

        result = graph.invoke({
            "query": query,
            "intent": "",
            "response": ""
        })

        st.success(result["response"])

    else:
        st.warning("Please enter a question.")