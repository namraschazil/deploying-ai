import os
from dotenv import load_dotenv

import chromadb
from chromadb.utils import embedding_functions
from pathlib import Path

load_dotenv("/Users/namraschazil/deploying-ai/05_src/.secrets")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Missing OPENAI_API_KEY in .env file")

def embed_documents():
    client = chromadb.PersistentClient(path="/Users/namraschazil/deploying-ai/05_src/assignment_chat/chroma_db")

    embedding_function = embedding_functions.OpenAIEmbeddingFunction(
        api_key=OPENAI_API_KEY,
        model_name="text-embedding-3-small"
    )

    collection = client.get_or_create_collection(
        name="policies",
        embedding_function=embedding_function
    )

    policy_folder = Path("/Users/namraschazil/deploying-ai/05_src/assignment_chat/policies")
    documents = []
    ids = []

    for file in policy_folder.glob("*.txt"):
        with open(file, "r", encoding="utf-8") as f:
            text = f.read()
            documents.append(text)
            ids.append(file.stem)

    collection.add(
        documents=documents,
        ids=ids
    )

    print("Documents embedded successfully!")

if __name__ == "__main__":
    embed_documents()