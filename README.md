# 📄 PDF-QA-System

An intelligent **Retrieval-Augmented Generation (RAG)** application that enables users to interact with PDF documents using natural language. The system extracts text from uploaded PDFs, converts it into semantic vector embeddings, retrieves the most relevant content using FAISS similarity search, and generates context-aware responses using Google's Gemini Large Language Model (LLM).

---

## 🚀 Features

* 📂 Upload one or multiple PDF documents
* 📑 Automatic text extraction using PyPDF2
* ✂️ Intelligent text chunking for efficient retrieval
* 🧠 Semantic embeddings using Google Generative AI Embeddings
* 🔍 Fast similarity search with FAISS Vector Store
* 🤖 Context-aware question answering with Google Gemini
* 💬 Interactive and user-friendly Streamlit interface
* ⚡ Real-time document-based conversational AI

---

## 🏗️ System Architecture

```text
                User Uploads PDF(s)
                        │
                        ▼
             PDF Text Extraction (PyPDF2)
                        │
                        ▼
        Recursive Character Text Splitting
                        │
                        ▼
      Google Generative AI Embeddings Model
                        │
                        ▼
              FAISS Vector Database
                        │
                        ▼
      Similarity Search (Relevant Chunks)
                        │
                        ▼
           Gemini Large Language Model
                        │
                        ▼
          Context-Aware Answer Generation
                        │
                        ▼
          Streamlit Web Application UI
```

---

## 🔄 Project Workflow

1. Upload one or more PDF documents.
2. Extract textual content from every uploaded PDF.
3. Split extracted text into overlapping chunks.
4. Convert every chunk into vector embeddings.
5. Store embeddings inside a FAISS vector database.
6. Accept a natural language question from the user.
7. Retrieve the most relevant document chunks using semantic similarity.
8. Send the retrieved context and user question to Gemini.
9. Display an accurate and context-aware answer.

---

## 🛠️ Technology Stack

### Programming Language

* Python

### Frameworks & Libraries

* Streamlit
* LangChain
* PyPDF2
* FAISS
* Google Generative AI (Gemini)
* python-dotenv

### AI Technologies

* Retrieval-Augmented Generation (RAG)
* Large Language Models (LLMs)
* Semantic Search
* Vector Embeddings

---

## 📂 Project Structure

```text
DocVerseX-RAG-Engine/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Project dependencies
├── .env                    # Google API Key (not committed)
├── README.md
└── faiss_index/            # Generated vector database
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/Mohanaprasath007/DocVerseX-RAG-Engine.git
cd DocVerseX-RAG-Engine
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## 📖 How RAG Works in This Project

```text
PDF
 │
 ▼
Extract Text
 │
 ▼
Split into Chunks
 │
 ▼
Generate Vector Embeddings
 │
 ▼
Store in FAISS
 │
 ▼
User Question
 │
 ▼
Semantic Similarity Search
 │
 ▼
Retrieve Relevant Chunks
 │
 ▼
Gemini LLM
 │
 ▼
Generate Final Answer
```

---

## 🎯 Key Concepts Demonstrated

* Retrieval-Augmented Generation (RAG)
* Vector Embeddings
* Semantic Search
* Large Language Models (LLMs)
* Prompt Engineering
* Document Question Answering
* Conversational AI

---

## 🔮 Future Enhancements

* OCR support for scanned PDFs
* Hybrid Search (BM25 + Vector Search)
* Local LLM integration (Llama, Gemma, Mistral)
* Chat history persistence
* Multi-document comparison
* Docker deployment
* User authentication
* Source citation and answer highlighting

---

## ⚠️ Note

This project is intended for educational and learning purposes. It demonstrates the architecture and implementation of a Retrieval-Augmented Generation (RAG) system using PDF documents and Google's Gemini models. Due to frequent updates in AI frameworks and APIs, minor dependency or configuration changes may be required before running the application.

---

## 👨‍💻 Author

**Mohana Prasath M**

📧 Email: **[mohanaprasath.m2023@vitstudent.ac.in](mailto:mohanaprasath.m2023@vitstudent.ac.in)**

🌐 GitHub: **https://github.com/Mohanaprasath007**

💼 LinkedIn: **http://www.linkedin.com/in/mohana-prasath-119a47287**

---

## ⭐ Support

If you found this project helpful, please consider giving it a **⭐ Star** on GitHub.
