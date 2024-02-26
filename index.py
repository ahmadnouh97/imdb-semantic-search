import os
import ast
import pandas as pd
import chromadb

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')


data_dir = os.path.join("data")
processed_dir = os.path.join(data_dir, "processed")
index_dir = os.path.join(data_dir, "index")

os.makedirs(index_dir, exist_ok=True)

data = pd.read_csv(
    os.path.join(processed_dir, "data.csv"),
    index_col=False,
    converters={'vector': ast.literal_eval}
)

client = chromadb.PersistentClient(path=index_dir)

collection = client.get_or_create_collection(
    "imdb_movies",
)

collection.add(
    ids=[str(i) for i in list(range(1, len(data) + 1))],
    embeddings=data["vector"].tolist(),
    documents=data["orig_title"].tolist(),
    metadatas=data.drop(columns=["vector"]).to_dict(orient="records")
)