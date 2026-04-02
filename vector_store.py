from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from ingest import docs

load_dotenv()

def create_vector_store():
    embedding=OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embedding)
    db.save_local("faiss_index")
    
    print(f"Faiss Index created successfully")

if __name__ == "__main__":
    create_vector_store()