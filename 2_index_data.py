from pathlib import Path

import qdrant_client
from llama_index import (
    VectorStoreIndex,
    ServiceContext,
    download_loader,
)
from llama_index.llms import Ollama
from llama_index.storage.storage_context import StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore

# load the JSON off disk
JSONReader = download_loader("JSONReader")
loader = JSONReader()
documents = loader.load_data(Path('./data/tinytweets.json'))

# initialize the vector store
client = qdrant_client.QdrantClient(
    path="./qdrant_data"
)
vector_store = QdrantVectorStore(client=client, collection_name="tweets")
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# initialize the LLM
llm = Ollama(model="mixtral")
service_context = ServiceContext.from_defaults(llm=llm,embed_model="local")

# create the index; this will embed the documents and store them in the vector store
index = VectorStoreIndex.from_documents(documents,service_context=service_context,storage_context=storage_context)

# query the index
query_engine = index.as_query_engine()
response = query_engine.query("What does the author think about Star Trek? Give details.")
print(response)
