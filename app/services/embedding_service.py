from sentence_transformers import SentenceTransformer


# Load model only once (important for performance)
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def generate_embeddings(texts):

    embeddings = embedding_model.encode(
        texts,
        convert_to_numpy=True
    )

    return embeddings