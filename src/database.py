import json
import chromadb
from chromadb.utils import embedding_functions

# Create a persistent ChromaDB client
client = chromadb.PersistentClient(path="chroma_db")

# Use the default embedding model
embedding_function = embedding_functions.DefaultEmbeddingFunction()

# Create or get the collection
collection = client.get_or_create_collection(
    name="sports_facts",
    embedding_function=embedding_function
)


def load_data():
    """Load sports facts from JSON file."""

    with open("data/sports_facts.json", "r", encoding="utf-8") as file:
        return json.load(file)


def populate_database():
    """Insert facts into ChromaDB."""

    data = load_data()

    # Avoid inserting duplicate data
    if collection.count() > 0:
        print("✅ Database already populated.")
        return

    documents = []
    metadatas = []
    ids = []

    for index, item in enumerate(data):
        documents.append(item["fact"])
        metadatas.append({"sport": item["sport"]})
        ids.append(str(index))

    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )

    print(f"✅ Added {len(documents)} facts to ChromaDB.")


def search_facts(sport, query, n_results=3):
    """Retrieve relevant facts."""

    results = collection.query(
        query_texts=[query],
        n_results=n_results,
        where={"sport": sport}
    )

    return results["documents"][0]


# Run directly
if __name__ == "__main__":
    populate_database()