from pdf_ingestion import extract_text_from_pdf, chunk_text

# Test PDF path
pdf_path = "sample.pdf"  # Replace with the path to your PDF

# Test text extraction
text = extract_text_from_pdf(pdf_path)
assert len(text) > 0, "Text extraction failed!"

# Test text chunking
chunks = chunk_text(text, chunk_size=500)
assert len(chunks) > 0, "Chunking failed!"
print("PDF ingestion tests passed!")