from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import qdrant_client
from llama_index.llms import Ollama
from llama_index import (
    VectorStoreIndex,
    ServiceContext,
)
from llama_index.vector_stores.qdrant import QdrantVectorStore

# re-initialize the vector store
client = qdrant_client.QdrantClient(
    path="./qdrant_data"
)
vector_store = QdrantVectorStore(client=client, collection_name="tweets")

# get the LLM again
llm = Ollama(model="mixtral")
service_context = ServiceContext.from_defaults(llm=llm,embed_model="local")

# load the index from the vector store
index = VectorStoreIndex.from_vector_store(vector_store=vector_store,service_context=service_context)

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# This is just so you can easily tell the app is running
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/process_form', methods=['POST'])
@cross_origin()
def process_form():
    query = request.form.get('query')
    if query is not None:
        # query your data!
        # here we have customized the number of documents returned per query to 20, because tweets are really short
        query_engine = index.as_query_engine(similarity_top_k=20)
        response = query_engine.query(query)
        return jsonify({"response": str(response)})
    else:
        return jsonify({"error": "query field is missing"}), 400

if __name__ == '__main__':
    app.run()
