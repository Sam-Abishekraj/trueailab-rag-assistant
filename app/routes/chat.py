from fastapi import APIRouter

from app.models.request_models import (
    ChatRequest
)
from app.models.response_models import (
    ChatResponse
)

from app.services.document_loader import (
    load_documents
)
from app.services.chunking_service import (
    chunk_documents
)
from app.services.embedding_service import (
    generate_embeddings
)
from app.services.retrieval_service import (
    search_documents
)
from app.services.rag_service import (
    ask_rag
)

router = APIRouter()


@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    result = ask_rag(
        request.sessionId,
        request.message
    )

    return ChatResponse(
        reply=result["reply"],
        tokensUsed=result["tokensUsed"],
        retrievedChunks=result[
            "retrievedChunks"
        ]
    )


@router.get("/documents")
def get_documents():

    documents = load_documents()

    return {
        "total_documents": len(documents),
        "documents": [
            doc["title"]
            for doc in documents
        ]
    }


@router.get("/chunks")
def get_chunks():

    documents = load_documents()

    chunks = chunk_documents(
        documents
    )

    return {
        "total_chunks": len(chunks),
        "sample_chunk": chunks[0]
    }


@router.get("/embeddings")
def test_embeddings():

    documents = load_documents()

    chunks = chunk_documents(
        documents
    )

    sample_text = chunks[0]["content"]

    embedding = generate_embeddings(
        [sample_text]
    )

    return {
        "embedding_dimension": len(
            embedding[0]
        ),
        "sample_values":
            embedding[0][:10].tolist()
    }


@router.get("/search")
def search(query: str):

    results = search_documents(
        query
    )

    return results