import os
import ast
import pandas as pd

# Use the bundled SQLite on Linux; Python supplies SQLite on other platforms.
import sys
if sys.platform.startswith('linux'):
    __import__('pysqlite3')
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import chromadb


data_dir = os.path.join("data")
processed_dir = os.path.join(data_dir, "processed")
index_dir = os.path.join(data_dir, "index-v1")

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

# Chroma limits the number of records per request. Upsert makes reruns safe.
batch_size = client.get_max_batch_size()
for start in range(0, len(data), batch_size):
    batch = data.iloc[start:start + batch_size]
    collection.upsert(
        ids=[str(i) for i in range(start + 1, start + len(batch) + 1)],
        embeddings=batch["vector"].tolist(),
        documents=batch["orig_title"].tolist(),
        metadatas=batch.drop(columns=["vector"]).to_dict(orient="records")
    )
