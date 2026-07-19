import chromadb

from app.rag.embeddings import EmbeddingModel


class MedicalRetriever:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="app/chroma_db"
        )

        self.collection = self.client.get_collection(
            name="medical_knowledge"
        )

        self.embedder = EmbeddingModel()


    def search(self, query, top_k=3):

        query_embedding = self.embedder.create_embeddings(
            [query]
        )


        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=top_k
        )


        return results["documents"][0]



if __name__ == "__main__":

    retriever = MedicalRetriever()


    symptoms = """
    Patient has difficulty breathing,
    chest tightness and cough
    """


    results = retriever.search(symptoms)


    print("\nRelevant Medical Knowledge:\n")

    for i, result in enumerate(results):

        print(f"--- Result {i+1} ---")
        print(result[:500])
        print()