from config import generate
from utils.prompts import SUMMARY_PROMPT
from langchain_core.prompts import PromptTemplate


def summarize_transcript(transcript: str) -> str:
    template = PromptTemplate.from_template(SUMMARY_PROMPT)
    formatted_prompt = template.format(context=transcript)
    return generate(formatted_prompt)