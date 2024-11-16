from langchain_ollama import OllamaEmbeddings
from langchain_aws import BedrockEmbeddings

USE_LOCAL = True

def get_embedding_function():
    if USE_LOCAL:
        embeddings = OllamaEmbeddings(model="nomic-embed-text")
    else: 
        embeddings = BedrockEmbeddings(
            credentials_profile_name="default", region_name="us-east-1"
        )
    return embeddings
