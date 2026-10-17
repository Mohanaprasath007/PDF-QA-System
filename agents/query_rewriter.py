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


def rewrite_query(state):

    question = state["question"]

    prompt = f"""
You are a Query Rewriting Agent.

The previous retrieval was not sufficiently relevant.

Rewrite the user's question into a better search query.

The rewritten query should:

- preserve the original meaning
- include important keywords
- remove unnecessary words
- be specific
- improve semantic retrieval

Original question:

{question}

Return ONLY the rewritten search query.
"""

    response = llm.invoke(prompt)

    rewritten_query = get_response_text(response).strip()

    return {
        "rewritten_query": rewritten_query,
        "retry_count": state.get("retry_count", 0) + 1
    }