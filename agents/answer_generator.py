from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

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


def generate_answer(state):

    question = state["question"]

    context = state.get("context", "")

    prompt = f"""
You are the Answer Generation Agent in an Agentic RAG system.

Answer the user's question using the retrieved information.

Rules:

1. Use the provided context as the primary evidence.
2. Do not invent facts.
3. If the context does not contain enough information,
   clearly say that the information is insufficient.
4. Give a clear and concise answer.
5. Do not mention internal agents or implementation details.

Context:

{context}

Question:

{question}

Answer:
"""

    response = llm.invoke(prompt)

    answer = get_response_text(response).strip()

    return {
        "answer": answer
    }