import os
import pandas as pd
import streamlit as st

data_dir = os.path.join("data")
raw_dir = os.path.join(data_dir, "raw")

st.set_page_config(
    page_title="Preview Data",
    page_icon="📄",
    layout="wide"
)

st.title("Preview Data 📄")

@st.cache_data
def load_data():
    return pd.read_csv(os.path.join(raw_dir, "imdb_movies.csv"), index_col=False)

with st.container():
    with st.spinner():
        st.dataframe(load_data())