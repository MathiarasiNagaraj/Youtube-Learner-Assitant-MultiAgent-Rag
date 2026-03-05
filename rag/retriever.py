from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


def get_recommendations(query: str):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    results = vectorstore.similarity_search(query, k=3)

    return [
        {
            "title": r.metadata["title"],
            "difficulty": r.metadata["difficulty"],
            "description": r.page_content[:200]
        }
        for r in results
    ]