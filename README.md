# Mixtral 8x7b and LlamaIndex

This is a quick demo of how to get a fully local model up and running with Mixtral 8x7b and LlamaIndex; check out the accompanying [blog post](https://TKTKTK) for more details.

## Install dependencies

```
poetry shell
poetry install
```

## 1_smoketest.py

After you've downloaded [Ollama](https://ollama.ai/) and run `ollama run mixtral` run this to make sure everything is connected.

## 2_index_data.py

This will index the data in the `data` folder. You can run this as many times as you want, and it will only index new data.

## 3_verify_index.py

This demonstrates the working index without re-loading the documents.

## app.py

A very simple Flask app that demonstrates how to use the index in a web app. Note that `flask run` will not work; you must run `python app.py`.
