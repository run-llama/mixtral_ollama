# Just runs .complete to make sure the LLM is listening
from llama_index.llms import Ollama

llm = Ollama(model="mixtral")

response = llm.complete("Who is Laurie Voss?")
print(response)
