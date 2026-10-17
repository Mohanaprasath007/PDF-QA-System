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


def analyze_query(state):

    question = state["question"]

    prompt = f"""
You are the Query Analysis Agent in an Agentic RAG system.

Classify the user's question into exactly ONE category.

PDF:
The question can be answered using the uploaded PDF documents.

WEB:
The question requires current, latest, recent, external,
or internet-based information.

HYBRID:
The question requires information from both the uploaded
PDF documents and current/external web information.

User question:
{question}

Return ONLY one word:

PDF
WEB
HYBRID
"""

    response = llm.invoke(prompt)

    query_type = get_response_text(response).strip().upper()

    if query_type not in ["PDF", "WEB", "HYBRID"]:
        query_type = "PDF"

    return {
        "query_type": query_type,
        "retry_count": 0
    }