from app.services.document_loader import (
    load_documents
)
from app.services.chunking_service import (
    chunk_documents
)
from app.services.embedding_service import (
    generate_embeddings
)
from app.vectorstore.faiss_store import (
    FAISSVectorStore
)


vector_store = FAISSVectorStore()


def initialize_vector_store():

    documents = load_documents()

    chunks = chunk_documents(
        documents
    )

    texts = [
        chunk["content"]
        for chunk in chunks
    ]

    embeddings = generate_embeddings(
        texts
    )

    vector_store.build_index(
        embeddings,
        chunks
    )

    return vector_store


def search_documents(
    query,
    top_k=5,
    threshold=0.48
):
    
    enhanced_query = f"""
    {query}

    attendance eligibility
    attendance percentage
    exam eligibility
    minimum attendance
    attendance below 65 percent
    attendance condonation
    """

    query_embedding = generate_embeddings(
        [enhanced_query]
    )[0]

    results = vector_store.search(
        query_embedding,
        top_k
    )

    filtered_results = []

    for result in results:

        if result["score"] >= threshold:
            filtered_results.append(
                result
            )

    return filtered_results