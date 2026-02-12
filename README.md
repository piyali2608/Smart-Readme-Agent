# SmartReadmeAgent

## Overview
`SmartReadmeAgent` automates `README.md` generation for Python projects. It uses LangChain and Google Gemini (LLM) to analyze project structure and content, producing comprehensive READMEs. The agent integrates Faiss for vector pi, enabling Retrieval Augmented Generation (RAG) to enhance content quality. Built with FastAPI, it provides a high-performance API.

## Usage
1.  **Clone** this repository.
2.  **Install dependencies**: `pip install -r requirements.txt`
3.  **Set environment variables**: `GOOGLE_API_KEY`, `LANGCHAIN_API_KEY` (optional).
4.  **Run the API**: `python -m streamlit run app.py`

Access API docs at `http://localhost:8501/docs`.