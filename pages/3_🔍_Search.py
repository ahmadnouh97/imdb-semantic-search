import os
# override the old sqlite3
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import chromadb
import streamlit as st


data_dir = os.path.join("data")
processed_dir = os.path.join(data_dir, "processed")
index_dir = os.path.join(data_dir, "index")

st.set_page_config(
    page_title="Search Data",
    page_icon="🔍",
    layout="wide"
)

@st.cache_resource
def get_collection():
    client = chromadb.PersistentClient(path=index_dir)
    return client.get_collection("imdb_movies")

@st.cache_data
def search(query: str):
    return collection.query(
        query_texts=[query],
        n_results=5,
        include=["documents", "distances", "metadatas"]
    )


collection = get_collection()

st.title("Search Data 🔍")

with st.container():
    query = st.text_input("Write a query", value="a movie about two magicians who compete against each others")
    if query:
        with st.spinner("Wait for it..."):
            result = search(query)

        documents = result.get("documents")[0]
        metadatas = result.get("metadatas")[0]
        
        for document, metadata in zip(documents, metadatas):
            st.markdown(f"## {document}")
            st.text(metadata.get("overview"))
            st.divider()