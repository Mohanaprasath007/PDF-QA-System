from typing import TypedDict, List, Any


class AgentState(TypedDict, total=False):

    # User's original question
    question: str

    # Query rewritten by the agent
    rewritten_query: str

    # PDF / WEB / HYBRID
    query_type: str

    # Retrieved PDF documents
    documents: List[Any]

    # Web search results
    web_results: List[Any]

    # Combined context given to Gemini
    context: str

    # Generated answer
    answer: str

    # Evaluator result
    retrieval_score: float

    # Whether retrieved information is sufficient
    retrieval_ok: bool

    # Verification result
    verification_result: str

    # Number of retrieval attempts
    retry_count: int