import argparse
import os
import json
from query_data import query_rag
from populate_database import clear_database, load_documents, load_single_pdf, split_documents, add_to_chroma

PDF_DIRECTORY = "C:\\Users\\user\\Experiment\\pfe-book-parser\\pageParser\\pdfs_test_double"


def process_pdf(pdf_file, query_text):
    pdf_name = os.path.splitext(os.path.basename(pdf_file))[0].lower()
    print("pdf_name", pdf_name)

    output_folder = "results"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # Clear existing database
    clear_database()

    # Load documents from PDF
    documents = load_single_pdf(pdf_file)

    # Split documents into chunks
    chunks = split_documents(documents)

    # Add documents to the database
    add_to_chroma(chunks, pdf_name)

    # Run query
    query_results = query_rag(query_text, pdf_name)

    # Save output as text
    output_filename = os.path.join(output_folder, pdf_name + ".txt")
    with open(output_filename, "w") as f:
        f.write(query_results)


def process_pdfs_in_folder(folder, query_text):
    for filename in os.listdir(folder):
        try:
            if filename.endswith(".pdf"):
                pdf_file = os.path.join(folder, filename)
                print(f"Processing PDF: {pdf_file}")
                process_pdf(pdf_file, query_text)
        except Exception as e:
            print("An error occurred:", e)



def main():
    # Create CLI
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="Query text.")
    args = parser.parse_args()
   # folder = args.folder
    query_text = args.query_text

    # Process PDF files in the folder
    process_pdfs_in_folder(PDF_DIRECTORY, query_text)


if __name__ == "__main__":
    main()
