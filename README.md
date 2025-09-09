# RAG Tutorial v2

This project demonstrates a Retrieval-Augmented Generation (RAG) pipeline using LangChain, ChromaDB, and Ollama for local LLM and embedding inference. It features both a command-line interface and a **minimalistic web-based chat UI** built with Streamlit.

## 🚀 Quick Start - Web Interface

1. Make sure you have followed all setup steps in the sections below.
2. Start the Ollama server (if not already running):
	```
	ollama serve
	```
3. Launch the minimalistic chat interface:
	```
	streamlit run app.py
	```
4. Open your browser to the provided URL (usually `http://localhost:8501`)
5. Upload PDF documents directly through the web interface or use existing files
6. Start chatting with your documents!

## 🖥️ Command Line Interface

For traditional command-line usage:

1. (Optional) Add or update PDF files in the `data/` directory.
2. Populate the database:
	```
	python populate_database.py
	```
3. Run a query:
	```
	python query_data.py "Your question here"
	```

## ✨ Features

### Web Interface (app.py)
- **Minimalistic Design**: Clean, distraction-free chat interface
- **File Upload**: Drag-and-drop PDF upload with real-time processing
- **Interactive Chat**: Conversation history with user-friendly message bubbles
- **Collapsible Upload**: Hide/show document upload section to focus on chat
- **Real-time Processing**: Instant document ingestion and querying
- **Settings Panel**: Clear chat history and reset database
- **Responsive Design**: Works well on desktop and mobile devices

### Core RAG Pipeline
- **Document Processing**: Automatic PDF text extraction and chunking
- **Vector Database**: ChromaDB for efficient similarity search
- **Local LLM**: Mistral model via Ollama (no API keys required)
- **Local Embeddings**: Nomic-embed-text model for text embeddings
- **Smart Retrieval**: Context-aware document retrieval for accurate answers

## 📁 Project Structure

```
rag-tutorial-v2/
├── app.py                      # Streamlit web interface (minimalistic design)
├── query_data.py              # Command-line querying
├── populate_database.py       # Database population utilities
├── get_embedding_function.py  # Embedding model configuration
├── test_rag.py               # Testing utilities
├── requirements.txt          # Python dependencies
├── data/                     # PDF documents directory
│   └── ath.pdf              # Example document
└── chroma/                   # ChromaDB vector store
    └── chroma.sqlite3       # Vector database file
```

## 🎨 UI Design Features

The Streamlit interface features a **minimalistic design philosophy**:

- **Clean Layout**: Centered layout with optimal reading width
- **Minimal Visual Clutter**: Hidden Streamlit branding and unnecessary elements
- **Modern Chat Bubbles**: Distinct styling for user and assistant messages
- **Smooth Interactions**: Hover effects and transitions for better UX
- **Collapsible Sections**: Upload area can be hidden to focus on conversation
- **Color Scheme**: Subtle grays and blues for a professional appearance
- **Typography**: Clean, readable fonts with proper spacing
- **Responsive**: Adapts to different screen sizes

## Prerequisites
- Python 3.10+
- [Ollama](https://ollama.com/) installed and running locally
- (Optional) AWS credentials if using Bedrock embeddings

## Setup Instructions

### 1. Clone the Repository
```
git clone <your-repo-url>
cd rag-tutorial-v2
```

### 2. Install Python Dependencies
```
pip install -r requirements.txt
```

### 3. Download Ollama Models
You need the following models:
- `nomic-embed-text` (for embeddings)
- `mistral` (for LLM)

Pull them using:
```
ollama pull nomic-embed-text
ollama pull mistral
```

### 4. Add Your PDF Files
Place your PDF files in the `data/` directory. Example:
```
data/
	monopoly.pdf
	ticket_to_ride.pdf
	your_file.pdf
```

### 5. Populate the Vector Database
This step processes all PDFs and creates the Chroma vector store:
```
python populate_database.py
```

### 6. Query the Data
Ask questions using the RAG pipeline:
```
python query_data.py "Your question here"
```
Example:
```
python query_data.py "How much total money does a player start with in Monopoly?"
```

## Usage Examples

### Web Interface
1. **Upload a Document**: Click "Add Document" and select a PDF file
2. **Ask Questions**: Type your question in the chat input
3. **View Responses**: See AI responses with context from your documents
4. **Manage Chat**: Use sidebar to clear chat or reset database

### Command Line
```bash
# Process documents
python populate_database.py

# Ask questions
python query_data.py "What is the main topic of the document?"
python query_data.py "How much money does each player start with?"
python query_data.py "What are the rules for passing GO?"
```

## Updating Data

### Web Interface
- Simply upload new PDF files through the web interface
- Documents are automatically processed and added to the vector database
- No manual database population needed

### Command Line
If you add new PDFs to the `data/` directory, run:
```bash
python populate_database.py
```

## Notes
- If you see deprecation warnings, consider updating imports as suggested in the warnings.
- To use AWS Bedrock embeddings, update `get_embedding_function.py` and configure your AWS credentials.

## Troubleshooting

### Common Issues
- **Ollama Connection**: Ensure Ollama is running (`ollama serve`)
- **Model Not Found**: Pull required models (`ollama pull mistral` and `ollama pull nomic-embed-text`)
- **Streamlit Port**: If port 8501 is busy, Streamlit will suggest an alternative
- **File Upload**: Ensure PDF files are valid and not password-protected
- **Memory Issues**: For large documents, consider splitting them into smaller files

### Performance Tips
- Use the web interface for better user experience
- Upload smaller PDF files for faster processing
- Clear the database periodically if it becomes too large
- Close the upload section to focus on chat interface

## Tech Stack

- **Frontend**: Streamlit with custom CSS for minimalistic design
- **Backend**: Python with LangChain framework
- **Vector Database**: ChromaDB for similarity search
- **LLM**: Mistral via Ollama (local inference)
- **Embeddings**: Nomic-embed-text (local embeddings)
- **Document Processing**: PyPDF for PDF text extraction

## License
MIT
