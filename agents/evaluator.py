import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


def get_response_text(response):
    content = response.content

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        text_parts = []

        for item in content:
            if isinstance(item, dict):
                text_parts.append(item.get("text", ""))
            else:
                text_parts.append(str(item))

        return "".join(text_parts)

    return str(content)


def evaluate_retrieval(state):

    question = state["question"]

    documents = state.get("documents", [])

    web_results = state.get("web_results", [])

    context_parts = []

    for doc in documents:
        context_parts.append(doc.page_content)

    for result in web_results:
        context_parts.append(
            result.get("content", "")
        )

    context = "\n\n".join(context_parts)

    if not context.strip():
        return {
            "retrieval_score": 0.0,
            "retrieval_ok": False,
            "context": ""
        }

    prompt = f"""
You are a Retrieval Evaluation Agent.

Determine whether the retrieved information is sufficient
to answer the user's question.

Question:
{question}

Retrieved information:
{context}

Give a relevance score from 0 to 10.

10 = highly relevant and sufficient
7-9 = relevant and mostly sufficient
4-6 = partially relevant
1-3 = mostly irrelevant
0 = completely irrelevant

Return ONLY the number.
"""

    response = llm.invoke(prompt)

    response_text = get_response_text(response).strip()

    try:
        score = float(response_text)
    except ValueError:
        score = 0.0

    score = max(0.0, min(score, 10.0))

    retrieval_ok = score >= 7

    return {
        "retrieval_score": score,
        "retrieval_ok": retrieval_ok,
        "context": context
    }