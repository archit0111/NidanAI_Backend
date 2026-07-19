from app.rag.retriever import Retriever
from app.rag.prompt_builder import PromptBuilder
from app.llm.gemini import generate_response


class ChatService:

    def __init__(self):
        self.retriever = Retriever()

    def chat(self, query: str):

        # Retrieve relevant medical knowledge
        retrieved_docs = self.retriever.search(query)

        # Build prompt
        prompt = PromptBuilder.build(
            user_query=query,
            retrieved_docs=retrieved_docs
        )

        # Ask Gemini
        answer = generate_response(prompt)

        return {
            "query": query,
            "retrieved": retrieved_docs,
            "response": answer
        }