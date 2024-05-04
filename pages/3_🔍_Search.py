import os
import chromadb
import streamlit as st


data_dir = os.path.join("data")
processed_dir = os.path.join(data_dir, "processed")
index_dir = os.path.join(data_dir, "index")

client = chromadb.PersistentClient(path=index_dir)

collection = client.get_collection(
    "imdb_movies",
)

st.set_page_config(
    page_title="Search Data",
    page_icon="🔍",
    layout="wide"
)

st.title("Search Data 🔍")

with st.container():
    text_search = st.text_input("Write a query", value="a movie about two magicians who compete against each others")
    if text_search:
        with st.spinner("Wait for it..."):
            result = collection.query(
                query_texts=[text_search],
                n_results=5,
                include=["documents", "distances", "metadatas"]
            )

        documents = result.get("documents")[0]
        metadatas = result.get("metadatas")[0]
        
        for document, metadata in zip(documents, metadatas):
            st.markdown(f"## {document}")
            st.text(metadata.get("overview"))
            st.divider()