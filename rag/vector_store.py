import json
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings


def build_vectorstore():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    with open("data/leetcode_problems.json") as f:
        data = json.load(f)

    docs = [
        Document(
            page_content=item["description"],
            metadata={
                "title": item["title"],
                "difficulty": item["difficulty"]
            }
        )
        for item in data
    ]

    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local("faiss_index")