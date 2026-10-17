from tavily import TavilyClient
from dotenv import load_dotenv
import os

from ingestion.vector_store import load_vector_store


load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

tavily_client = TavilyClient(
    api_key=TAVILY_API_KEY
)


def retrieve_from_pdf(state):

    question = state.get("rewritten_query", state["question"])

    vector_store = load_vector_store()

    documents = vector_store.similarity_search(
        question,
        k=5
    )

    return {
        "documents": documents
    }


def retrieve_from_web(state):

    question = state.get("rewritten_query", state["question"])

    response = tavily_client.search(
        query=question,
        search_depth="advanced",
        max_results=5
    )

    web_results = response.get("results", [])

    return {
        "web_results": web_results
    }


def retrieve_hybrid(state):

    question = state.get("rewritten_query", state["question"])

    # PDF retrieval
    vector_store = load_vector_store()

    documents = vector_store.similarity_search(
        question,
        k=5
    )

    # Web retrieval
    response = tavily_client.search(
        query=question,
        search_depth="advanced",
        max_results=5
    )

    web_results = response.get("results", [])

    return {
        "documents": documents,
        "web_results": web_results
    }