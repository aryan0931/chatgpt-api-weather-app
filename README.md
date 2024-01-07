# ChatGPT Python API for Weather Information

<img width="1279" alt="Screenshot 2023-12-29 at 2 45 25 PM" src="https://github.com/aryan0931/chatgpt-api-python-sales/assets/141573833/ae7ba5ef-a0b6-4ab0-8f9d-e70d6f3bb861">


This is an AI app to provide **real-time** weather information from various locations around the world. The project exposes an HTTP REST endpoint to answer user queries about the current weather conditions in a specific location or from a given input file (such as CSV, JSONlines, PDF, Markdown, Txt). It uses Pathway’s [LLM App features](https://github.com/pathwaycom/llm-app) to build a real-time LLM (Large Language Model)-enabled data pipeline in Python, leveraging OpenAI API [Embeddings](https://platform.openai.com/docs/api-reference/embeddings) and [Chat Completion](https://platform.openai.com/docs/api-reference/completions) endpoints to generate AI assistant responses.

## Features

- Retrieves the latest weather information from various sources.
- Provides an API interface to explore current weather conditions.
- Offers a user-friendly UI with [Streamlit](https://streamlit.io/).
- Filters and presents weather information based on user queries or chosen data sources.
- Data and code reusability for offline evaluation. Users have the option to choose to use local (cached) or real data.
- Extend data sources: Using Pathway's built-in connectors for JSONLines, CSV, Kafka, Redpanda, Debezium, streaming APIs, and more.

## Further Improvements

There are more things you can achieve, and here are upcoming features:

- Incorporate additional data from external APIs, along with various files (such as Jsonlines, PDF, Doc, HTML, or Text format), databases like PostgreSQL or MySQL, and stream data from platforms like Kafka, Redpanda, or Debedizum.
- Merge data from these sources instantly.
- Maintain a data snapshot to observe variations in weather conditions over time, as Pathway provides a built-in feature to compute **differences** between two alterations.
- Beyond making data accessible via API or UI, the LLM App allows you to relay processed data to other downstream connectors, such as BI and analytics tools. For instance, set it up to **receive alerts** upon detecting weather shifts.



In case you use OpenWeatherMap API as a data source for the project, it provides real-time weather information for various locations.

Code sample

It requires only a few lines of code to build a real-time AI-enabled data pipeline:

import pathway as pw

from common.embedder import embeddings, index_embeddings
from common.prompt import prompt


def run(host, port):
    # Given a user question as a query from your API
    query, response_writer = pw.io.http.rest_connector(
        host=host,
        port=port,
        schema=QueryInputSchema,
        autocommit_duration_ms=50,
    )

    # Real-time data coming from external data sources such as jsonlines file
  sales_data = pw.io.jsonlines.read(
        "./examples/data",
        schema=DataInputSchema,
        mode="streaming"
    )

    # Compute embeddings for each document using the OpenAI Embeddings API
   embedded_data = embeddings(context=sales_data, data_to_embed=sales_data.doc)

    # Construct an index on the generated embeddings in real-time
   index = index_embeddings(embedded_data)

    # Generate embeddings for the query from the OpenAI Embeddings API
   embedded_query = embeddings(context=query, data_to_embed=pw.this.query)

      # Build prompt using indexed data
  responses = prompt(index, embedded_query, pw.this.query)

    # Feed the prompt to ChatGPT and obtain the generated answer.
  response_writer(responses)

    # Run the pipeline
  pw.run()


class DataInputSchema(pw.Schema):
    doc: str


class QueryInputSchema(pw.Schema):
    query: str



Use case

Open AI GPT excels at answering questions, but only on topics it remembers from its training data. If you want GPT to answer questions about unfamiliar topics such as:

~Real-time weather conditions.
~Specific details about weather in a given location.
~Current atmospheric conditions.
~The model might not answer such queries properly. Because it is not aware of the context or historical data or it needs additional details. In this case, you can use LLM App efficiently to give context to this search or answer process. See how LLM App works.

How the project works

The sample project does the following procedures to achieve the above output:

Prepare search data:
Collect: You choose a data source or upload the CSV file through the UI file-uploader, and it maps each row into a JSONline schema for better managing large data sets.
Chunk: Documents are split into short, mostly self-contained sections to be embedded.
Embed: Each section is embedded with the OpenAI API and retrieve the embedded result.
Indexing: Constructs an index on the generated embeddings.

Search (once per query)

Given a user question, generate an embedding for the query from the OpenAI API.
Using the embeddings, retrieve the vector index by relevance to the query

Ask (once per query)

Insert the question and the most relevant sections into a message to GPT
Return GPT's answer
How to run the project

Example only supports Unix-like systems (such as Linux, macOS, BSD). If you are a Windows user, we highly recommend leveraging Windows Subsystem for Linux (WSL) or Dockerize the app to run as a container.

Run with Docker

~Set environment variables
~From the project root folder, open your terminal and run docker compose up.
~Navigate to localhost:8501 on your browser when docker installation is successful.

Prerequisites

~Make sure that Python 3.10 or above installed on your machine.
~Download and Install Pip to manage project packages.
~Create an OpenAI account and generate a new API Key: To access the ~OpenAI API, you will need to create an API Key. You can do this by logging into the OpenAI website and navigating to the API Key management page.

https://github.com/aryan0931/chatgpt-api-weather-app/assets/141573833/5e198075-38a4-4acf-9f1f-6e308b0e8b1c

