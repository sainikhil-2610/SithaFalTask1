from transformers import pipeline
from sentence_transformers import SentenceTransformer

def handle_query(query, index, chunks):
    # Generate embedding for the query
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = model.encode([query])[0]

    # Retrieve relevant chunks
    relevant_chunks = search_faiss(index, query_embedding, chunks)

    # Generate response with LLM
    generator = pipeline('text2text-generation', model='google/flan-t5-large')
    context = " ".join(relevant_chunks)
    return generator(f"Context: {context}\nQuestion: {query}", max_length=200)[0]['generated_text']
# query_handling.py (additional function)
def handle_comparison(query,chunks):
    # Identify terms to compare (e.g., via regex or prompt parsing)
    #terms = extract_comparison_terms(query)
    comparison_data = []
    for chunk in chunks:
           if "comparison" in query:
               comparison_data.append(chunk)
    response="\n".join(f"-{data}"
         for data in comparison_data)    
    return response          

    # Retrieve relevant data
    results = []
    for term in terms:
        query_embedding = generate_embeddings([term])[0]
        results.append(search_faiss(index, query_embedding, chunks))

    # Generate structured response
    response = format_comparison_response(results)
    return response
# query_handling.py (extended response generation)
def format_comparison_response(results):
    # Example: Create a tabular response
    response = "Comparison Results:\n"
    for i, result in enumerate(results):
        response += f"Field {i+1}:\n"
        response += "\n".join(result)
    return response
def extract_specific_data(text, page_number):
    if page_number == 2:
        # Use regex for unemployment data
        return extract_unemployment_data(text)
    elif page_number == 6:
        # Parse tabular data
        return extract_tabular_data(text)

"""from transformers import pipeline
from sentence_transformers import SentenceTransformer

def handle_query(query, index, chunks):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = model.encode([query])[0]
    relevant_chunks = search_faiss(index, query_embedding, chunks)

    generator = pipeline('text2text-generation', model='google/flan-t5-large')
    context = " ".join(relevant_chunks)
    return generator(f"Context: {context}\nQuestion: {query}", max_length=200)[0]['generated_text']"""