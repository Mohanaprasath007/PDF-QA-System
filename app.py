import os

import streamlit as st

from dotenv import load_dotenv

from ingestion.pdf_loader import extract_pdf_text

from ingestion.text_chunker import create_text_chunks

from ingestion.vector_store import create_vector_store

from graph.workflow import build_graph


# --------------------------------
# Environment
# --------------------------------

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


if not GOOGLE_API_KEY:

    st.error("GOOGLE_API_KEY not found in .env")

    st.stop()


if not TAVILY_API_KEY:

    st.error("TAVILY_API_KEY not found in .env")

    st.stop()


# --------------------------------
# Page configuration
# --------------------------------

st.set_page_config(
    page_title="DocVerseX Agentic RAG",
    page_icon="📚",
    layout="wide"
)


st.title("📚 DocVerseX Agentic RAG")

st.write(
    "Ask questions from your PDFs or current information "
    "from the web using an adaptive Agentic RAG workflow."
)


# --------------------------------
# Build graph
# --------------------------------

agent_graph = build_graph()


# --------------------------------
# Sidebar
# --------------------------------

with st.sidebar:

    st.header("Document Processing")

    pdf_docs = st.file_uploader(
        "Upload PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    process_button = st.button(
        "Process Documents"
    )


# --------------------------------
# Process PDFs
# --------------------------------

if process_button:

    if not pdf_docs:

        st.warning(
            "Please upload at least one PDF."
        )

    else:

        with st.spinner(
            "Processing documents..."
        ):

            raw_text = extract_pdf_text(
                pdf_docs
            )

            if not raw_text.strip():

                st.error(
                    "No readable text was found in the PDFs."
                )

                st.stop()

            chunks = create_text_chunks(
                raw_text
            )

            create_vector_store(
                chunks
            )

        st.success(
            f"Processed {len(chunks)} text chunks."
        )


# --------------------------------
# User question
# --------------------------------

question = st.text_input(
    "Ask a question"
)


if question:

    if not os.path.exists(
        "faiss_index"
    ):

        st.warning(
            "Please upload and process a PDF first."
        )

        st.stop()

    with st.spinner(
        "Agent is thinking..."
    ):

        initial_state = {
            "question": question,
            "retry_count": 0
        }

        result = agent_graph.invoke(
            initial_state
        )


    # --------------------------------
    # Display result
    # --------------------------------

    st.subheader("Answer")

    st.write(
        result.get(
            "answer",
            "No answer generated."
        )
    )


    # --------------------------------
    # Agent information
    # --------------------------------

    with st.expander(
        "Agent Execution Details"
    ):

        st.write(
            "Query Type:",
            result.get(
                "query_type"
            )
        )

        st.write(
            "Retrieval Score:",
            result.get(
                "retrieval_score"
            )
        )

        st.write(
            "Retry Count:",
            result.get(
                "retry_count"
            )
        )

        st.write(
            "Verification:",
            result.get(
                "verification_result"
            )
        )

        if result.get(
            "rewritten_query"
        ):

            st.write(
                "Rewritten Query:",
                result.get(
                    "rewritten_query"
                )
            )