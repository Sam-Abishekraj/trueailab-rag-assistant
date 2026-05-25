import faiss
import numpy as np


class FAISSVectorStore:

    def __init__(self):

        self.index = None
        self.metadata = []

    def build_index(
        self,
        embeddings,
        metadata
    ):

        embeddings = np.array(
            embeddings,
            dtype="float32"
        )

        # Normalize for cosine similarity
        faiss.normalize_L2(
            embeddings
        )

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatIP(
            dimension
        )

        self.index.add(
            embeddings
        )

        self.metadata = metadata

    def search(
        self,
        query_embedding,
        top_k=3
    ):

        query_embedding = np.array(
            [query_embedding],
            dtype="float32"
        )

        faiss.normalize_L2(
            query_embedding
        )

        scores, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for score, idx in zip(
            scores[0],
            indices[0]
        ):

            if idx == -1:
                continue

            results.append({
                "score": float(score),
                "chunk": self.metadata[idx]
            })

        return results