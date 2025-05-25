# RAG Tutorial v2

## Best Practices

### 🔑 Key Requirements

- **Use the exact embedding function for both scenarios**: The same vector embedding function MUST be used for:
  - Storing data in vector database
  - Querying the database
  - LangChain has many different embedding functions - refer to [LangChain documentation on embedding functions](https://python.langchain.com/docs/integrations/text_embedding/)

- **Document Loaders**: Various document loaders are available for different document types:
  - CSV
  - Markdown
  - HTML
  - MS Office
  - JSON
  - Refer to [LangChain documentation on document loaders](https://python.langchain.com/docs/integrations/document_loaders/)

## Current Problem: HuggingFace Models in Two Places

### Overview

HuggingFace is used in **two different places** in your RAG system:

### 1. 📊 Embeddings (`get_embedding_function.py`)

```python
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2",
    model_kwargs={'device': 'cpu'},
    encode_kwargs={'normalize_embeddings': True}
)
```

**Purpose**: Convert text into numerical vectors (embeddings) for similarity search

- **Input**: Text chunks from your PDFs
- **Output**: Vector representations (arrays of numbers)
- **Used for**: Finding similar documents when you search

### 2. 🤖 Language Model (`query_data.py`)

```python
from langchain_community.llms import HuggingFacePipeline

model = HuggingFacePipeline.from_model_id(
    model_id="microsoft/DialoGPT-small",
    task="text-generation",
    model_kwargs={"temperature": 0.7, "max_length": 512}
)
```

**Purpose**: Generate human-like responses based on the retrieved context

- **Input**: Your question + relevant document chunks
- **Output**: Natural language answer
- **Used for**: Creating the final response to your question

## 🔄 Why Both Are Needed

```mermaid
graph TD
    A[Your Question: "How many clues can I give in Codenames?"] --> B[HuggingFace Embeddings: Convert question to vector]
    B --> C[Find similar docs]
    C --> D[Retrieved relevant text chunks from database]
    D --> E[HuggingFace LLM: Generate answer from question + context]
    E --> F[Final Answer]
```

## ⚠️ The Problem in Your Case

1. **✅ Embeddings work fine** - they found documents (just wrong ones)
2. **❌ Language Model is poor** - DialoGPT-small gives garbled responses

## 💡 Better Alternatives

### For Embeddings (Keep This - It's Working)

```python
# This is fine, keep using it
HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
```

### For Language Model (Replace This)

```python
# Instead of HuggingFacePipeline, use:
from langchain_openai import ChatOpenAI
model = ChatOpenAI(model="gpt-3.5-turbo")  # Much better responses
```

## 📋 Installation Requirements

```bash
# For improved embeddings
pip install -U langchain-huggingface langchain-chroma

# For OpenAI integration
pip install langchain-openai

# Set your API key
export OPENAI_API_KEY="your-api-key-here"
```

## 🎯 Conclusion

The **embeddings part** works well with HuggingFace, but the **text generation part** needs a better model like OpenAI GPT or Claude for good results.

### Recommended Setup:
- **Embeddings**: HuggingFace (`all-MiniLM-L6-v2`)
- **Language Model**: OpenAI (`gpt-3.5-turbo`) or Claude

This combination gives you:
- Fast, local embeddings for document retrieval
- High-quality language model for response generation