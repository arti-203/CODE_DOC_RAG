<<<<<<< HEAD
# CODE_DOC_RAG
=======

# Code Documentation RAG System

## Overview
A Retrieval-Augmented Generation (RAG) system to analyze GitHub repositories, understand multi-language code, and generate context-aware explanations.

## Features
- Fetch GitHub repo files
- Generate embeddings for code and docs
- Answer questions using RAG with OpenAI GPT-4o
- Multi-language syntax understanding

## Tech Stack
- Python, Streamlit
- OpenAI GPT-4o embeddings
- ChromaDB for vector search
- PyGithub for GitHub integration

## Run Locally
1. Clone repo
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Add `.env` file with your OpenAI API key
4. Run:
   ```
   streamlit run app.py
   ```
>>>>>>> e4a54d9 (Initial commit - Code Documentation RAG project)
