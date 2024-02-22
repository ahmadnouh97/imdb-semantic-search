# IMDB Semantic Search

**Agenda:**

- [Introduction](#introduction)
- [Installation](#installation)
- [Technologies Used](#technologies-used)
- [About](#about)

## Introduction

Welcome to **IMDB Semantic Search**! This Streamlit application allows you to perform semantic searches on IMDb movies using a ChromDB (Vector Database). By leveraging semantic search techniques, you can find movies based on their meaning rather than just keywords.

## Installation

To run this application locally, follow these steps:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/imdb-semantic-search.git
```

2. Navigate to the project directory:

```bash
cd imdb-semantic-search
```

3. Initialize your environment using Poetry:

```bash
poetry init
```

4. Install the required dependencies:

```bash
poetry install
```

5. Activate environment by running:
    ```bash
    source .venv/Scripts/activate # For windows
    ``` 
    or
    ```bash
    source .venv/bin/activate # For Linux & Mac
    ```

6. Index data by running:
    ```bash
    python index.py
    ```

7. Run the Streamlit application:

```bash
streamlit run 1_🏠_Home.py
```


## Technologies Used

- **Streamlit**: This application is built using Streamlit, a powerful framework for creating data-centric web applications with simple Python scripts.

- **ChromDB (Vector Database)**: The semantic search functionality is powered by ChromDB, a vector database that enables efficient storage and retrieval of vectorized data. ChromDB utilizes Sentence Transformer, specifically the all-MiniLM-L6-v2 model, to calculate the embeddings of the data.

- **Sentence Transformer (all-MiniLM-L6-v2 model)**: This model is employed within ChromDB to convert textual data into numerical vectors, facilitating semantic similarity calculations. It plays a crucial role in enabling effective semantic search capabilities within the application.

- **IMDb Dataset**: The application utilizes [IMDb dataset](https://www.kaggle.com/datasets/ashpalsingh1525/imdb-movies-dataset?resource=download) for movie information including names, genre, date, crew, and others.


## About

This application was developed by Ahmad Nouh. It demonstrates the implementation of semantic search techniques for IMDb movies using Streamlit and ChromDB. Feel free to explore, modify, and use this application for learning and personal projects.

For any questions or feedback, please reach out to Ahmad Nouh at [ahmadnouh428@gmail.com].

Enjoy searching for your favorite movies with ease using **IMDB Semantic Search**!