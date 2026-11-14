import os

import numpy as np
import pandas as pd
import streamlit as st
from sentence_transformers import SentenceTransformer

from semantic_search import nearest_movies

st.set_page_config(page_title="Search Data", page_icon="🔍", layout="wide")


@st.cache_resource
def load_search_data():
    data = pd.read_csv(
        os.path.join("data", "processed", "data.csv"),
        converters={"vector": lambda value: np.fromstring(value[1:-1], sep=",", dtype=np.float32)},
    )
    vectors = np.asarray(data.pop("vector").tolist(), dtype=np.float32)
    return data, vectors


@st.cache_resource
def load_model():
    return SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


@st.cache_data
def search(query):
    data, vectors = load_search_data()
    query_vector = load_model().encode(query, normalize_embeddings=True)
    return data.iloc[nearest_movies(vectors, query_vector)]


st.title("Search Data 🔍")
with st.container():
    query = st.text_input("Write a query", value="a movie about two magicians who compete against each others")
    if query:
        with st.spinner("Wait for it..."):
            results = search(query)
        for _, movie in results.iterrows():
            st.markdown(f"## {movie['orig_title']}")
            st.text(movie["overview"])
            st.divider()
