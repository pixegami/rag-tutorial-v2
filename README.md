# rag-tutorial-v2

This repository is a starter guide for learning how to use Retrieval-Augmented Generation (RAG) with Ollama. Follow the steps below to set up and run the project.

## Prerequisites

Ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd rag-tutorial-v2
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Setting Up the Database

1. Place your PDF documents in the [data](http://_vscodecontentref_/0) directory.

2. Populate the database with the documents:
    ```sh
    python populate_database.py --reset
    ```

## Querying the Database

To query the database, run the [query_data.py](http://_vscodecontentref_/1) script with your query text:
```sh
python query_data.py "Your query text here"
```
## Project Structure

- `__pycache__/`: Directory containing Python bytecode files.
- `.gitignore`: Git ignore file to specify untracked files to ignore.
- `chroma/`: Directory containing the Chroma database files.
  - `77943a61-1aef-45fe-af55-a29fb829e25b/`: Subdirectory for Chroma database.
  - `chroma.sqlite3`: SQLite database file for Chroma.
- `data/`: Directory to store PDF documents.
- `get_embedding_function.py`: Script to get the embedding function.
- `populate_database.py`: Script to populate the Chroma database with documents.
- `query_data.py`: Script to query the Chroma database.
- `README.md`: This README file.
- `requirements.txt`: List of required Python packages.
- `test_rag.py`: Script to run tests on the RAG setup.