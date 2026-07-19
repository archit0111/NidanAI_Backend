from app.rag.knowledge_base import MedicalKnowledgeBase


kb = MedicalKnowledgeBase()

knowledge = kb.build()

print(knowledge.head())

print()

print(knowledge.columns)