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

## 🔄 RAG Workflow Explanation

The assistant follows a Retrieval-Augmented Generation (RAG) pipeline to generate grounded responses.

### Step 1: User Query
The user asks a university-related question.

Example:

```text
Can I write exams with 60% attendance?
```

### Step 2: Query Embedding
The user query is converted into vector embeddings using the embedding model.

### Step 3: Similarity Search
The query embedding is compared against stored document embeddings inside the FAISS vector database.

Top relevant chunks are retrieved.

### Step 4: Context Injection
Retrieved policy chunks are inserted into a carefully designed prompt.

### Step 5: LLM Response Generation
Gemini generates a grounded answer strictly using retrieved policy context.

### Step 6: Follow-up Understanding
Chat history is preserved for contextual conversations.

Example:

User:
```text
What is minimum attendance?
```

Follow-up:

```text
What if I am below that?
```

The assistant understands contextual references.

## 🔍 Embedding Strategy Explanation

To enable semantic search and contextual retrieval:

1. University policy documents are loaded from `docs.json`.
2. Large documents are split into smaller chunks.
3. Each chunk is converted into vector embeddings.
4. Embeddings are stored inside a FAISS vector database.

When a user asks a question:

- The question is converted into embeddings.
- Similar chunks are retrieved.
- Retrieved context is injected into the prompt.

This ensures semantically relevant and grounded answers.

## 🎯 Similarity Search Explanation

The project uses vector similarity search through **FAISS**.

### Retrieval Process

1. Convert user query into embeddings.
2. Compare query vector against stored document vectors.
3. Rank chunks based on similarity score.
4. Retrieve Top-K relevant chunks.

Only the most relevant chunks are passed to Gemini.

This minimizes hallucination and improves answer accuracy.

## 🧩 Prompt Design Reasoning

The prompt was carefully designed to ensure accurate and grounded responses.

### Grounded Responses
The assistant must answer only using retrieved university policy context.

### Hallucination Prevention
The prompt explicitly prevents policy invention.

### Follow-up Question Understanding
Conversation history is included for contextual understanding.

### Rule Completeness
Important conditions, eligibility rules, and exceptions must not be omitted.

### Fallback Handling
If relevant information is unavailable:

```text
"I could not find enough information in the university knowledge base."
```

The assistant avoids making assumptions.

## 🔧 Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/trueailab-rag-assistant.git
```

### 2. Navigate to Project

```bash
cd trueailab-rag-assistant
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Environment

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create `.env`

```env
GEMINI_API_KEY=your_api_key_here
MODEL_NAME=gemini-2.5-flash
```

### 7. Run Backend

```bash
uvicorn app.main:app --reload
```

### 8. Run Frontend

```bash
cd frontend
python3 -m http.server 5500
```

Open:

```text
http://localhost:5500
```

## 📸 Screenshots

### Home Interface
<img width="1918" height="1029" alt="image" src="https://github.com/user-attachments/assets/b834b9bd-25ed-469f-92d2-fcba7d33bbdd" />


### Attendance Query
<img width="1918" height="1029" alt="image" src="https://github.com/user-attachments/assets/c5540139-042b-40ad-8225-9469c98abfb1" />


### Follow-up Question Handling
<img width="1918" height="1029" alt="image" src="https://github.com/user-attachments/assets/cf6690ca-33ed-463b-912a-08e1a95610ce" />


### Unknown Query Response
<img width="1918" height="1029" alt="image" src="https://github.com/user-attachments/assets/d32d8369-7b0e-4ec4-95f6-70dbd482f26c" />


### Swagger API Documentation
<img width="1918" height="1029" alt="image" src="https://github.com/user-attachments/assets/932645ae-dbd7-4ae5-a784-8ec6f364306a" />


### Railway Deployment
<img width="1918" height="1029" alt="image" src="https://github.com/user-attachments/assets/b77a1606-fd89-4058-881e-adc7004b3863" />


### Vercel Deployment
<img width="1918" height="1029" alt="image" src="https://github.com/user-attachments/assets/3ef26ca2-b890-4a33-8630-b0d9f1f07806" />

