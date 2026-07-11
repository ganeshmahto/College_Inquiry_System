from graph import build_graph

graph = build_graph()

query = input("Enter your question: ")

result = graph.invoke({
    "query": query,
    "intent": "",
    "response": ""
})

print("\n**RESULT**")
print(result["response"])





