#  TechVerse University RAG Assistant

An AI-powered Retrieval-Augmented Generation (RAG) chatbot designed to answer university policy-related questions using contextual document retrieval and Large Language Model (LLM) reasoning.

The assistant retrieves relevant university policies from a vector database and generates grounded responses using Google's Gemini API.

---

##  Live Demo

### Frontend (Vercel)
[My techverse university RAG Assitant](https://trueailab-rag-assistant-nine.vercel.app/)

### Backend API (Railway)
[My Web Production Backend](https://web-production-eb849.up.railway.app/docs#/)

---

##  Project Objective

University policies are often stored in long documents that students must manually search through.

This project solves that problem by building an intelligent **University Policy Assistant** capable of:

- Answering attendance-related questions
- Explaining examination eligibility
- Handling follow-up questions
- Retrieving policy-specific answers
- Preventing hallucinations using grounded context

---

##  Features

### Core Features
- Retrieval-Augmented Generation (RAG)
- Context-aware responses
- Follow-up question handling
- Similarity-based retrieval
- Policy-grounded answers
- Fallback response when information is unavailable
- Beautiful responsive frontend UI

### AI Features
- Gemini LLM integration
- Prompt engineering
- Vector similarity search
- Embedding-based retrieval
- Session-based chat memory

---

##  System Architecture

```text
User
   ↓
Frontend (Vercel)
   ↓ REST API
FastAPI Backend (Railway)
   ↓
Retrieval Service
   ↓
FAISS Vector Store
   ↓
Relevant Policy Chunks
   ↓
Prompt Builder
   ↓
Gemini API
   ↓
Final Response
