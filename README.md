# rag-tutorial-v2


## PDF Data

1. Download example PDF file in a subfolder `data`


## Ollma

1. Run the Ollama serve
2. Pull the `nomic-embed-text` model

## Populate the database

1. python populate_database.py


## Generate Embeddings

1. python get_embedding_function.py


## Run Query

1. Update query_data.py to use the required model
2. Run the command:
```python
python query_data.py "QUERY"
```

