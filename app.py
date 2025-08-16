
import streamlit as st
from github_loader import fetch_github_repo
from rag_engine import build_rag_index, query_rag

st.title("Code Documentation RAG System")

repo_url = st.text_input("Enter GitHub Repo URL")
if st.button("Load Repo"):
    with st.spinner("Fetching repo..."):
        repo_files = fetch_github_repo(repo_url)
        build_rag_index(repo_files)
        st.success(f"Loaded {len(repo_files)} files.")

query = st.text_input("Ask about the repo")
if st.button("Get Answer"):
    with st.spinner("Generating answer..."):
        answer = query_rag(query)
        st.markdown(f"**Answer:**\n\n{answer}")
