from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embedding_function():
    # Option 1: Use Ollama embeddings (requires Ollama to be installed and running)
    # Uncomment this if you have Ollama installed with an embedding model
    # embeddings = OllamaEmbeddings(model="nomic-embed-text")
    
    # Option 2: Use HuggingFace embeddings (downloads model locally, no API key needed)
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2",  # Good balance of performance and speed
        model_kwargs={'device': 'cpu'},  # Use 'cuda' if you have GPU
        encode_kwargs={'normalize_embeddings': True}
    )
    
    return embeddings