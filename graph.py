from langgraph.graph import StateGraph, START, END

from state import CollegeState

from nodes.intent_classifier import intent_classifier
from nodes.admission_agent import admission_agent
from nodes.exam_agent import exam_agent
from nodes.fees_agent import fees_agent
from nodes.scholarship_agent import scholarship_agent
from nodes.response_agent import response_agent


def route_by_intent(state: CollegeState):

    intent = state.get("intent", "").strip().lower()

    routes = {
        "admission": "admission_agent",
        "exam": "exam_agent",
        "fees": "fees_agent",
        "scholarship": "scholarship_agent",
    }

    return routes.get(intent, "admission_agent")


def build_graph():

    graph = StateGraph(CollegeState)

    graph.add_node("intent_classifier", intent_classifier)
    graph.add_node("admission_agent", admission_agent)
    graph.add_node("exam_agent", exam_agent)
    graph.add_node("fees_agent", fees_agent)
    graph.add_node("scholarship_agent", scholarship_agent)
    graph.add_node("response_agent", response_agent)

    graph.add_edge(START, "intent_classifier")

    graph.add_conditional_edges(
        "intent_classifier",
        route_by_intent,
        {
            "admission_agent": "admission_agent",
            "exam_agent": "exam_agent",
            "fees_agent": "fees_agent",
            "scholarship_agent": "scholarship_agent",
        },
    )

    graph.add_edge("admission_agent", "response_agent")
    graph.add_edge("exam_agent", "response_agent")
    graph.add_edge("fees_agent", "response_agent")
    graph.add_edge("scholarship_agent", "response_agent")

    graph.add_edge("response_agent", END)

    return graph.compile()









# Project Created by Ganesh Kumar Mahto , Date: 11-07-2026, Branch: CSE-2 , Registration No: 24040445012
# Collage: Dumka Engineering College, Dumka, Jharkhand, India 