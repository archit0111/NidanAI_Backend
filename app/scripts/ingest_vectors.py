from app.rag.knowledge_base import MedicalKnowledgeBase
from app.rag.embeddings import EmbeddingModel
from app.rag.vector_store import VectorStore


print("Loading Knowledge Base...")

kb = MedicalKnowledgeBase()

knowledge = kb.build()

print(f"Loaded {len(knowledge)} diseases")


embedding_model = EmbeddingModel()

vector_store = VectorStore()


for _, row in knowledge.iterrows():

    text = f"""
Disease: {row['Disease']}

Description:
{row['Description']}

Medication:
{row['Medication']}

Diet:
{row['Diet']}

Precautions:
{row['Precaution_1']}
{row['Precaution_2']}
{row['Precaution_3']}
{row['Precaution_4']}

Workout:
{row['Workouts']}
"""

    embedding = embedding_model.encode(text)

    vector_store.add(
        doc_id=row["Disease"],
        document=text,
        embedding=embedding,
        metadata={
            "disease": row["Disease"]
        },
    )

print()

print("Knowledge Indexed Successfully!")

print("Total Documents:", vector_store.count())