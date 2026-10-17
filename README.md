# 📚 DocVerseX-RAG-Engine

An intelligent **Agentic Retrieval-Augmented Generation (Agentic RAG)** application that enables users to ask questions about PDF documents and retrieve relevant information from the web. Built with Python, LangChain, LangGraph, Google Gemini, Hugging Face embeddings, FAISS, and Tavily, the system uses an adaptive workflow to analyze queries, select a retrieval strategy, evaluate retrieved information, rewrite queries when necessary, and generate context-aware answers.

## 🚀 Features

- 📂 **PDF Upload and Processing:** Upload one or multiple PDF documents.
- 📄 **PDF Text Extraction:** Extract document text using PyPDF2.
- ✂️ **Intelligent Text Chunking:** Split extracted content into overlapping chunks for efficient retrieval.
- 🧠 **Semantic Embeddings:** Generate vector embeddings using Hugging Face Sentence Transformers.
- 🔍 **FAISS Vector Search:** Retrieve relevant document chunks using semantic similarity.
- 🌐 **Web Search:** Retrieve current, relevant information using Tavily.
- 🔀 **Adaptive Retrieval:** Route questions to PDF, web, or hybrid retrieval based on query analysis.
- 🤖 **Agentic Workflow:** Orchestrate retrieval, evaluation, rewriting, generation, and verification using LangGraph.
- ♻️ **Query Rewriting:** Refine queries when the retrieved information is insufficient.
- 📊 **Retrieval Evaluation:** Evaluate retrieval relevance and decide whether another retrieval attempt is needed.
- ✅ **Answer Verification:** Run a verification step to assess generated answers.
- 💬 **Interactive Interface:** Ask questions through a Streamlit web application.
- 🐳 **Docker Containerization:** Package the application and its Python dependencies into a Docker image.

## 🏗️ System Architecture

```text
                   User Question
                         │
                         ▼
                  Query Analyzer
                         │
                         ▼
                 Retrieval Router
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
          PDF Search  Web Search  Hybrid Search
              │          │          │
              ▼          ▼          ▼
             FAISS      Tavily    FAISS + Tavily
              │          │          │
              └──────────┼──────────┘
                         ▼
                 Retrieval Evaluator
                         │
                ┌────────┴────────┐
                │                 │
          Relevant Enough?    Insufficient?
                │                 │
                ▼                 ▼
         Answer Generator    Query Rewriter
                ▲                 │
                │                 ▼
                │          Retry Retrieval
                │                 │
                └─────────────────┘
                         │
                         ▼
                  Gemini LLM
                         │
                         ▼
                  Answer Verifier
                         │
                         ▼
                 Final Answer
                         │
                         ▼
                  Streamlit UI
```

*Note: The diagram represents the intended workflow. The exact execution path depends on the query and retrieval evaluation results.*

## 🔄 How the Agentic RAG Workflow Works

1. **Query Analysis:** Analyze the user's question and determine whether PDF, web, or hybrid retrieval is appropriate.
2. **Retrieval Routing:** Direct the query to the selected retrieval method.
3. **PDF Retrieval:** Search the FAISS vector store for relevant document chunks.
4. **Web Retrieval:** Use Tavily to search for relevant web information.
5. **Hybrid Retrieval:** Combine PDF and web retrieval when both sources are useful.
6. **Retrieval Evaluation:** Evaluate the retrieved information to determine whether it is sufficiently relevant.
7. **Query Rewriting:** If retrieval is inadequate, rewrite the query and attempt retrieval again, subject to the retry limit.
8. **Answer Generation:** Use Google Gemini to generate a response based on the available context.
9. **Answer Verification:** Pass the generated response through a verification step.
10. **Response Display:** Display the resulting answer and workflow details in Streamlit.

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Frontend | Streamlit |
| LLM Orchestration | LangChain, LangGraph |
| Large Language Model | Google Gemini API |
| Embedding Model | Hugging Face Sentence Transformers |
| Vector Database | FAISS |
| Web Search | Tavily |
| PDF Processing | PyPDF2 |
| Environment Configuration | python-dotenv |
| Containerization | Docker, Docker Desktop |

## 📂 Project Structure

```text
DocVerseX-RAG-Engine/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .env
│
├── ingestion/
│   ├── __init__.py
│   ├── pdf_loader.py
│   ├── text_chunker.py
│   └── vector_store.py
│
├── agents/
│   ├── __init__.py
│   ├── query_analyzer.py
│   ├── retriever.py
│   ├── evaluator.py
│   ├── query_rewriter.py
│   ├── answer_generator.py
│   └── verifier.py
│
├── graph/
│   ├── __init__.py
│   ├── state.py
│   └── workflow.py
│
└── faiss_index/
```

**Directory overview:**

- `app.py`: Streamlit user interface and application entry point.
- `ingestion/`: PDF text extraction, text chunking, and vector-store creation.
- `agents/`: Query analysis, retrieval, evaluation, query rewriting, answer generation, and verification.
- `graph/`: Shared agent state and LangGraph workflow orchestration.
- `faiss_index/`: Locally persisted FAISS vector index generated during document processing.
- `Dockerfile`: Instructions for building the application image.
- `.dockerignore`: Files and directories excluded from the Docker build context.
- `requirements.txt`: Python dependency list.
- `.env`: Local environment variables and API credentials.

## ⚙️ Installation and Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Mohanaprasath007/DocVerseX-RAG-Engine.git
cd DocVerseX-RAG-Engine
```

### 2. Create a Virtual Environment

Python 3.11 is used as the base version in the Docker configuration.

```bash
python -m venv venv
```

### 3. Activate the Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```bat
venv\Scripts\activate.bat
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Replace the placeholders with your actual API keys. Never commit `.env` to GitHub.

### 6. Run the Application

```bash
streamlit run app.py
```

Open the application at:

**http://localhost:8501**

## 🐳 Docker Setup

Docker packages the application and its dependencies into a portable image, reducing differences between development and deployment environments.

### Prerequisites

- Docker Desktop installed on Windows, macOS, or Linux.
- Docker Engine running.
- Valid Google Gemini and Tavily API keys.

### 1. Build the Docker Image

Run this command from the project root, where the `Dockerfile` is located:

```bash
docker build -t docvertex-rag .
```

### 2. Run the Container

Pass API credentials through the local `.env` file:

```bash
docker run --env-file .env -p 8501:8501 docvertex-rag
```

Open **http://localhost:8501** in your browser.

### 3. Persist the FAISS Index

To preserve the generated vector index when a container is removed or recreated, use a named Docker volume:

```bash
docker run --env-file .env -p 8501:8501 -v docvertex_data:/app/faiss_index docvertex-rag
```

This command persists the FAISS index directory. It does not automatically preserve the original uploaded PDF files.

**Security note:** Keep API keys outside the Docker image. Exclude `.env` from the Docker build context using `.dockerignore`, and supply it at runtime.

## 🧠 Core AI Concepts Demonstrated

- Agentic Retrieval-Augmented Generation (Agentic RAG)
- Large Language Models (LLMs)
- Semantic Vector Embeddings
- FAISS Similarity Search
- Adaptive Retrieval Routing
- Query Rewriting and Retrieval Retry
- Retrieval Evaluation
- Answer Verification
- Prompt Engineering
- LangGraph State-Based Workflow Orchestration
- PDF Question Answering
- Web-Augmented Information Retrieval
- Docker Containerization

## 🔮 Future Enhancements

- OCR support for scanned PDFs.
- BM25 and vector-based hybrid ranking.
- Persistent chat history and conversational memory.
- Source citations with document page references and web URLs.
- Improved retrieval evaluation using reranking models.
- More robust answer verification and hallucination detection.
- Authentication and multi-user document management.
- Cloud deployment on AWS.
- CI/CD automation for Docker image builds and deployment.
- Monitoring, logging, and performance evaluation.

## ⚠️ Notes and Limitations

- Web search requires a valid Tavily API key.
- Answer generation requires a valid Google Gemini API key.
- The Hugging Face embedding model may need to be downloaded on the first run.
- The FAISS index must be created by processing documents before PDF retrieval can work.
- Web results depend on search availability and API limits.
- Retrieval evaluation and answer verification depend on the implemented agent logic and should not be treated as guarantees of factual correctness.
- Docker containerization packages the application, but cloud deployment requires additional infrastructure and configuration.

## 👨‍💻 Author

**Mohana Prasath M**

- 📧 Email: [mohanaprasath.m2023@vitstudent.ac.in](mailto:mohanaprasath.m2023@vitstudent.ac.in)
- 🌐 GitHub: [Mohanaprasath007](https://github.com/Mohanaprasath007)
- 💼 LinkedIn: [Mohana Prasath](https://www.linkedin.com/in/mohana-prasath-119a47287/)

---

⭐ If you find this project useful, consider giving the repository a star.
