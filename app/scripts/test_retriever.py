from app.rag.retriever import Retriever

print("Loading Retriever...")

retriever = Retriever()

print("Searching...")

results = retriever.search(
    "I have fever and headache for three days"
)

print()

for result in results:
    print("=" * 60)
    print("Disease :", result["id"])
    print("Score   :", result["score"])
    print("Metadata:", result["metadata"])
    print()