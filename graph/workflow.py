from langgraph.graph import StateGraph, START, END

from graph.state import AgentState

from agents.query_analyzer import analyze_query

from agents.retriever import (
    retrieve_from_pdf,
    retrieve_from_web,
    retrieve_hybrid
)

from agents.evaluator import evaluate_retrieval

from agents.query_rewriter import rewrite_query

from agents.answer_generator import generate_answer

from agents.verifier import verify_answer


def route_query(state):

    query_type = state.get(
        "query_type",
        "PDF"
    )

    return query_type


def evaluate_route(state):

    if state.get("retrieval_ok", False):

        return "GENERATE"

    retry_count = state.get(
        "retry_count",
        0
    )

    if retry_count >= 2:

        return "GENERATE"

    return "RETRY"


def retry_route(state):

    query_type = state.get(
        "query_type",
        "PDF"
    )

    retry_count = state.get(
        "retry_count",
        0
    )

    if retry_count >= 2:

        return "STOP"

    return query_type


def build_graph():

    graph = StateGraph(AgentState)

    graph.add_node(
        "query_analyzer",
        analyze_query
    )

    graph.add_node(
        "pdf_retriever",
        retrieve_from_pdf
    )

    graph.add_node(
        "web_retriever",
        retrieve_from_web
    )

    graph.add_node(
        "hybrid_retriever",
        retrieve_hybrid
    )

    graph.add_node(
        "evaluator",
        evaluate_retrieval
    )

    graph.add_node(
        "query_rewriter",
        rewrite_query
    )

    graph.add_node(
        "answer_generator",
        generate_answer
    )

    graph.add_node(
        "verifier",
        verify_answer
    )

    graph.add_edge(
        START,
        "query_analyzer"
    )

    graph.add_conditional_edges(
        "query_analyzer",
        route_query,
        {
            "PDF": "pdf_retriever",
            "WEB": "web_retriever",
            "HYBRID": "hybrid_retriever"
        }
    )

    graph.add_edge(
        "pdf_retriever",
        "evaluator"
    )

    graph.add_edge(
        "web_retriever",
        "evaluator"
    )

    graph.add_edge(
        "hybrid_retriever",
        "evaluator"
    )

    graph.add_conditional_edges(
        "evaluator",
        evaluate_route,
        {
            "RETRY": "query_rewriter",
            "GENERATE": "answer_generator"
        }
    )

    graph.add_conditional_edges(
        "query_rewriter",
        retry_route,
        {
            "PDF": "pdf_retriever",
            "WEB": "web_retriever",
            "HYBRID": "hybrid_retriever",
            "STOP": "answer_generator"
        }
    )

    graph.add_edge(
        "answer_generator",
        "verifier"
    )

    graph.add_edge(
        "verifier",
        END
    )

    return graph.compile()