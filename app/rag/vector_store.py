import chromadb
from chromadb.config import Settings

from app.rag.embeddings import EmbeddingModel


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="app/chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="medical_knowledge"
        )

        self.embedder = EmbeddingModel()


    def add_documents(self, documents):

        texts = []
        ids = []

        for index, doc in enumerate(documents):

            text = f"""
Disease: {doc['Disease']}

Description:
{doc['Description']}

Diet:
{doc['Diet']}

Medication:
{doc['Medication']}

Precautions:
{doc['Precaution_1']},
{doc['Precaution_2']},
{doc['Precaution_3']},
{doc['Precaution_4']}

Workout:
{doc['Workouts']}
"""

            texts.append(text)
            ids.append(str(index))


        embeddings = self.embedder.create_embeddings(texts)


        self.collection.add(
            documents=texts,
            embeddings=embeddings,
            ids=ids
        )


        print("✅ Medical knowledge added to ChromaDB")
        print("Total documents:", len(ids))



if __name__ == "__main__":

    import json


    with open(
        "app/datasets/medical_knowledge.json",
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)


    store = VectorStore()

    store.add_documents(data)