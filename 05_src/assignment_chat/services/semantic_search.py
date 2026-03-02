import chromadb
from chromadb.utils import embedding_functions

def initialize_chroma():
    client = chromadb.PersistentClient(path="./chroma_db")
    
    embedding_function = embedding_functions.OpenAIEmbeddingFunction(
        api_key="YOUR_OPENAI_KEY",
        model_name="text-embedding-3-small"
    )

    collection = client.get_or_create_collection(
        name="policies",
        embedding_function=embedding_function
    )
    
    return collection

def query_policies(collection, query):
    results = collection.query(
        query_texts=[query],
        n_results=2
    )
    
    documents = results["documents"][0]
    
    if not documents:
        return "I couldn't find relevant policy information."

    return "Here’s what I found:\n\n" + "\n\n".join(documents)