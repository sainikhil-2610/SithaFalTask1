# vector_store.py
import faiss
import numpy as np

def build_faiss_index(embeddings):
    dimension = len(embeddings[0])
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))
    return index

def search_faiss(index, query_embedding, chunks, top_k=5):
    distances, indices = index.search(np.array([query_embedding]), top_k)
    return [chunks[i] for i in indices[0]]
"""import faiss
import numpy as np

def build_faiss_index(embeddings):
    dimension = len(embeddings[0])
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))
    return index

def search_faiss(index, query_embedding, chunks, top_k=5):
    distances, indices = index.search(np.array([query_embedding]), top_k)
    return [chunks[i] for i in indices[0]]"""