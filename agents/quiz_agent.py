from langchain_core.prompts import PromptTemplate
from config import llm
from utils.prompts import QUIZ_PROMPT

def generate_quiz(summary: str):
    prompt = PromptTemplate.from_template(QUIZ_PROMPT)

    chain = prompt | llm

    response = chain.invoke({"context": summary})
    return response.content