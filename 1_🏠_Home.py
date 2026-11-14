import os
import streamlit as st


data_dir = os.path.join("data")
processed_dir = os.path.join(data_dir, "processed")
index_dir = os.path.join(data_dir, "index")


st.set_page_config(
    page_title="Semantic Search",
    page_icon="🏠",
    layout="wide"
)

st.title("Semantic Search")

introduction = """
## Introduction

Welcome to **IMDB Semantic Search**! This Streamlit application allows you to perform semantic searches on IMDb movies using precomputed movie embeddings. By leveraging semantic search techniques, you can find movies based on their meaning rather than just keywords.
"""

used_tech = """
## Technologies Used

- **Streamlit**: This application is built using Streamlit, a powerful framework for creating data-centric web applications with simple Python scripts.

- **NumPy**: The app ranks precomputed movie embeddings by squared Euclidean distance.

- **Sentence Transformer (all-MiniLM-L6-v2 model)**: This model is used to convert textual data into numerical vectors, facilitating semantic similarity calculations. It plays a crucial role in enabling effective semantic search capabilities within the application.

- **IMDb Dataset**: The application utilizes [IMDb dataset](https://www.kaggle.com/datasets/ashpalsingh1525/imdb-movies-dataset?resource=download) for movie information including names, genre, date, crew, and others.

"""

with st.container():
    st.markdown(introduction)
    start = st.button("Getting Started", type="primary")
    if start:
        st.switch_page(page="pages/3_🔍_Search.py")
    st.markdown(used_tech)
