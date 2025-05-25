import argparse
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import HuggingFacePipeline
from get_embedding_function import get_embedding_function

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text
    query_rag(query_text)

def query_rag(query_text: str):
    # Prepare the DB.
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=5)
    
    if not results:
        print("No relevant documents found.")
        return "No relevant documents found."

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    
    # Uncomment this line if you want to see the prompt being sent to the model
    # print("Prompt being sent to model:")
    # print(prompt)
    # print("="*50)

    try:
        # Option 1: Use HuggingFace Pipeline (completely local, no API key needed)
        model = HuggingFacePipeline.from_model_id(
            model_id="microsoft/DialoGPT-small",  # Small model for faster loading
            task="text-generation",
            model_kwargs={"temperature": 0.7, "max_length": 512}
        )
        
        response_text = model.invoke(prompt)
        
        sources = [doc.metadata.get("id", None) for doc, _score in results]
        formatted_response = f"Response: {response_text}\nSources: {sources}"
        print(formatted_response)
        return response_text
        
    except Exception as e:
        print(f"Error with HuggingFace model: {e}")
        print("Installing required packages...")
        print("Run: pip install transformers torch")
        return None

if __name__ == "__main__":
    main()