from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="mistral",
    temperature=0.5,
)

def generate(prompt: str) -> str:
    response = llm.invoke(prompt)
    return response.content