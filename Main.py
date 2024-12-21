# main.py
from pdf_ingestion import extract_text_from_pdf, chunk_text, generate_embeddings
from vector_store import build_faiss_index
from query_handling import handle_query, handle_comparison

# Step 1: Extract and process PDF
text = extract_text_from_pdf("sampledata.pdf")
chunks = chunk_text(text)
embeddings = generate_embeddings(chunks)
index = build_faiss_index(embeddings)

# Step 2: Handle user queries
query = "What is the unemployment rate for bachelor's degree holders?"
response = handle_query(query, index, chunks)
print("Response:", response)

# Step 3: Handle comparison queries
comparison_query = "Compare unemployment rates for different degrees."
comparison_response = handle_comparison(comparison_query, index, chunks)
print("Comparison Response:", comparison_response)

"""from pdf_ingestion import extract_text_from_pdf, chunk_text
from vector_store import build_faiss_index, search_faiss
from query_handling import handle_query

# Step 1: Extract text from PDF
pdf_path = "sample.pdf"  # Replace with your PDF path
text = extract_text_from_pdf(pdf_path)
chunks = chunk_text(text)

# Step 2: Generate embeddings
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(chunks)

# Step 3: Build vector store
index = build_faiss_index(embeddings)

# Step 4: Query handling
query = "What is the unemployment rate for bachelor's degree holders?"
response = handle_query(query, index, chunks)
print("Response:", response)"""