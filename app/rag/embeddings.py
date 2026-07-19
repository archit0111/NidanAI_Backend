from sentence_transformers import SentenceTransformer


class EmbeddingModel:

    def __init__(self):
        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def create_embeddings(self, texts):
        return self.model.encode(
            texts,
            show_progress_bar=True
        ).tolist()


if __name__ == "__main__":

    embedder = EmbeddingModel()

    sample = [
        "Asthma is a respiratory disease causing breathing problems",
        "Diabetes requires blood sugar management"
    ]

    vectors = embedder.create_embeddings(sample)

    print("Embeddings created")
    print("Vector size:", len(vectors[0]))