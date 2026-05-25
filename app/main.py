from fastapi import FastAPI
from fastapi.middleware.cors import (
    CORSMiddleware
)

from app.routes.chat import (
    router as chat_router
)

from app.services.retrieval_service import (
    initialize_vector_store
)

app = FastAPI(
    title="TechVerse University RAG Assistant",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.on_event("startup")
def startup_event():

    initialize_vector_store()

    print(
        "Vector store initialized"
    )


app.include_router(
    chat_router,
    prefix="/api",
    tags=["Chat"]
)


@app.get("/")
def root():

    return {
        "message":
        "TechVerse University "
        "RAG Assistant API "
        "is running"
    }


@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }