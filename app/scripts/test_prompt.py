from app.rag.retriever import MedicalRetriever
from app.rag.prompt_builder import MedicalPromptBuilder


retriever = MedicalRetriever()


knowledge = retriever.search(
    """
    Patient has breathing difficulty,
    cough and chest tightness
    """
)


builder = MedicalPromptBuilder()


prompt = builder.build(
    patient_data="""
    Age: 25
    Symptoms:
    breathing difficulty,
    cough
    """,
    knowledge=knowledge
)


print(prompt)