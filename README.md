GenAI YouTube Learning Assistant

A Retrieval-Augmented Generation (RAG) based AI assistant that processes YouTube videos to generate structured learning outputs such as summaries, quizzes, and key insights. The system extracts transcripts from YouTube videos and uses LLM-based reasoning with vector search to provide context-aware educational responses.

Features

Extracts transcripts from YouTube videos automatically

Generates concise video summaries

Creates quiz questions for knowledge testing

Produces learning insights and key takeaways

Uses vector search to retrieve relevant transcript chunks

Provides context-aware answers using LLMs

Architecture

The system follows a RAG (Retrieval-Augmented Generation) architecture.

Transcript Extraction

Fetch transcript from the YouTube video.

Text Processing

Clean and split transcript into smaller chunks.

Embedding Generation

Convert text chunks into vector embeddings using HuggingFace models.

Vector Storage

Store embeddings in FAISS for efficient similarity search.

Retrieval

Retrieve the most relevant transcript chunks for a query.

LLM Generation

Use a language model to generate summaries, quizzes, and insights from retrieved context.

Project Structure
youtube-genai-helper
│
├── agents
│   ├── summary_agent.py
│   ├── quiz_agent.py
│   └── insights_agent.py
│
├── utils
│   ├── transcript_extractor.py
│   ├── text_cleaner.py
│   └── chunker.py
│
├── vectorstore
│   └── faiss_store.py
│
├── main.py
├── requirements.txt
└── README.md
Tech Stack

Python

LangChain

FAISS (Vector Store)

HuggingFace Embeddings

Ollama (LLaMA3)

YouTube Transcript API

Installation

Clone the repository

git clone https://github.com/MathiarasiNagaraj/Youtube-Learner-Assitant-MultiAgent-Rag/
cd youtube-genai-helper

Create a virtual environment

python -m venv venv
source venv/bin/activate

Install dependencies

pip install -r requirements.txt

Install and run Ollama

Install Ollama and pull the LLaMA3 model:

ollama pull llama3
Usage

Run the application:

python main.py

Enter a YouTube video URL when prompted.

The system will:

Extract the transcript

Build embeddings

Generate summary, quiz questions, and insights

Example Output

Summary

Concise explanation of the video content

Quiz

Question 1

Question 2

Question 3

Key Insights

Important concepts explained from the video

Future Improvements

Multi-agent orchestration with specialized task agents

Support for multiple videos and playlists

Web interface for interactive learning

Persistent vector database storage

LeetCode or practice question recommendations

License

This project is for educational and learning purposes.
