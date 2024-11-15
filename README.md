# rag-tutorial-v2

## Install dependencies

Run this command to install dependenies in the `requirements.txt` file. 

```python
pip install -r requirements.txt
```

## Create database

Create the Chroma DB.

```python
python populate_database.py
```

## Query the database

Query the Chroma DB.

```python
python query_data.py "How does Alice meet the Mad Hatter?"
```

## Run unit test

Query the Chroma DB.

```python
pytest
```

> You'll also need to install [Ollama](https://ollama.com/) to run it locally as shown in the Youtube video: https://www.youtube.com/watch?v=2TJxpyO3ei4