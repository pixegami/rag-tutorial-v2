# Ollama Development Environment

## PDF Data Extraction

1. Example PDF files available in the `data` folder


## OLLAMA Environment

Start an interactive shell using Ollama + GEMMA.
Environment set up is automated and provides a working environment.

```bash
nix-shell --pure
```

## Ollama Shell

Manual environment, require Ollama to be running in the background.

1. Run the Ollama serve
```bash
ollama serve
```

2. Pull the `nomic-embed-text` model (or one of your choice)

```bash
ollama pull [model]
```

### Populate the database

1. python populate_database.py


### Generate Embeddings

1. python get_embedding_function.py


### Run Query

1. Update query_data.py to use the required model
2. Run the command:
```python
python query_data.py "QUERY"
```

