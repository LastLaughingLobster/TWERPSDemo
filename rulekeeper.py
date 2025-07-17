from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

def load_rulebook(path='TWERPS.pdf'):
    loader = PyPDFLoader(path)
    documents = loader.load()
    text = ''.join([doc.page_content for doc in documents])
    return text

def split_into_sections(text):
    sections = [
        "INTRODUCTION", "CHARACTER GENERATION", "THE COMBAT SYSTEM",
        "HOW TO DO EVERYTHING", "ADVENTURES", "Introductory Adventure:"
    ]
    chunks, mapping = [], {}
    for i, section in enumerate(sections):
        start = text.find(section)
        if start == -1: continue
        end = text.find(sections[i+1], start) if i+1 < len(sections) else len(text)
        chunk = text[start:end].strip()
        chunks.append(chunk)
        mapping[section] = chunk
    return chunks, mapping

def build_vectorstore(section_chunks):
    embeddings = OpenAIEmbeddings()
    return FAISS.from_texts(section_chunks, embeddings)

def predict_relevant_sections(vectorstore, query, k=3):
    docs = vectorstore.similarity_search(query, k=k)
    return [doc.page_content for doc in docs]
