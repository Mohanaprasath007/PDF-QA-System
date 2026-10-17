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


def verify_answer(state):

    question = state["question"]

    answer = state["answer"]

    context = state.get("context", "")

    prompt = f"""
You are an Answer Verification Agent.

Check whether the generated answer is supported by
the retrieved context.

Question:
{question}

Retrieved Context:
{context}

Generated Answer:
{answer}

Return exactly one of:

SUPPORTED
PARTIALLY_SUPPORTED
NOT_SUPPORTED
"""

    response = llm.invoke(prompt)

    result = get_response_text(response).strip().upper()

    if result not in [
        "SUPPORTED",
        "PARTIALLY_SUPPORTED",
        "NOT_SUPPORTED"
    ]:
        result = "PARTIALLY_SUPPORTED"

    return {
        "verification_result": result
    }