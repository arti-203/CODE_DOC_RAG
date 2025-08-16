
# import os
# from dotenv import load_dotenv
# load_dotenv()

# from openai import OpenAI
# from chromadb.utils import embedding_functions
# from chromadb import Client
# from chromadb.config import Settings
# from utils import chunk_text

# openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# client = Client(Settings(
#     chroma_db_impl="duckdb+parquet",
#     persist_directory="./embeddings"
# ))

# collection = client.get_or_create_collection(name="code_docs", embedding_function=embedding_functions.OpenAIEmbeddingFunction(
#     api_key=os.getenv("OPENAI_API_KEY"),
#     model_name="text-embedding-3-large"
# ))

# def build_rag_index(repo_files):
#     for file in repo_files:
#         chunks = chunk_text(file["content"])
#         for idx, chunk in enumerate(chunks):
#             collection.add(
#                 documents=[chunk],
#                 metadatas=[{"path": file["path"], "chunk": idx}],
#                 ids=[f"{file['path']}_{idx}"]
#             )

# def query_rag(query, top_k=5):
#     results = collection.query(
#         query_texts=[query],
#         n_results=top_k
#     )
#     context = "\n\n".join([doc for doc in results['documents'][0]])
#     prompt = f"""You are a helpful coding assistant. Use the following context from a GitHub repo to answer the question:

# Context:
# {context}

# Question:
# {query}

# Answer:
# """
#     response = openai_client.chat.completions.create(
#         model="gpt-4o",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response.choices[0].message.content

import os
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
from chromadb.utils import embedding_functions
from chromadb import PersistentClient  # <-- Use PersistentClient instead of Client
from utils import chunk_text

# Load OpenAI client
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize Chroma client using the new method
client = PersistentClient(path="./embeddings")

# Create or get collection with OpenAI embedding function
collection = client.get_or_create_collection(
    name="code_docs",
    embedding_function=embedding_functions.OpenAIEmbeddingFunction(
        api_key=os.getenv("OPENAI_API_KEY"),
        model_name="text-embedding-3-large"
    )
)

def build_rag_index(repo_files):
    for file in repo_files:
        chunks = chunk_text(file["content"])
        for idx, chunk in enumerate(chunks):
            collection.add(
                documents=[chunk],
                metadatas=[{"path": file["path"], "chunk": idx}],
                ids=[f"{file['path']}_{idx}"]
            )

def query_rag(query, top_k=5):
    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )
    context = "\n\n".join(results['documents'][0])
    prompt = f"""You are a helpful coding assistant. Use the following context from a GitHub repo to answer the question:

Context:
{context}

Question:
{query}

Answer:
"""
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
