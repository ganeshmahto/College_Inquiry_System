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



















 

# Project Created by Ganesh Kumar Mahto , Date: 11-07-2026, Branch: CSE-2 , Registration No: 24040445012
# Collage: Dumka Engineering College, Dumka, Jharkhand, India 