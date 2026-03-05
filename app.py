from utils.youtube_transcript import get_transcript
from utils.text_splitter import split_text

from agents.summarizer_agent import summarize_transcript
from agents.quiz_agent import generate_quiz
from agents.leetcode_agent import recommend_problems
from rag.vector_store import build_vectorstore
import os


def main():
    url = input("Enter YouTube URL: ").strip()

    print("\n📥 Fetching transcript...")
    transcript = get_transcript(url)
    print(f"Transcript length: {len(transcript)} characters")
    print("✂️ Splitting transcript...")
    chunks = split_text(transcript)

    print("🧠 Generating summary...")

    combined_summary = ""
    for chunk in chunks:
        summary = summarize_transcript(chunk)
        combined_summary += summary + "\n"

    print("\n===== FINAL SUMMARY =====\n")
    print(combined_summary)

    print("\n❓ Generating quiz...")
    quiz = generate_quiz(combined_summary)
    print("\n===== QUIZ =====\n")
    print(quiz)

    print("\n💻 Recommending LeetCode Problems...")

    if not os.path.exists("faiss_index"):
        build_vectorstore()

    recommendations = recommend_problems(combined_summary)

    for rec in recommendations:
        print("\n--------------------------------")
        print(f"Title: {rec['title']}")
        print(f"Difficulty: {rec['difficulty']}")
        print(f"Description: {rec['description']}")
        print("--------------------------------")


if __name__ == "__main__":
    main()