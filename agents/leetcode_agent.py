from rag.retriever import get_recommendations

def recommend_problems(summary: str):
    docs = get_recommendations(summary)  

    recommendations = []

    for doc in docs:
        recommendations.append({  
            "title": doc["title"],
            "difficulty": doc["difficulty"],
            "description": doc["description"]
        })

    return recommendations