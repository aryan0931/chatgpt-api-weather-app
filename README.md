# ChatGPT Weather Information API

![WhatsApp Image 2024-01-07 at 10 30 05 AM](https://github.com/aryan0931/chatgpt-api-weather-app/assets/141573833/9954a80d-e3dd-4ac4-ac10-9b61316a799a)


This project is an AI-powered application that provides real-time weather information from various locations around the world. It exposes an HTTP REST endpoint to answer user queries about the current weather conditions in a specific location or from various input file formats (CSV, JSONlines, PDF, Markdown, Txt). The application leverages Pathway’s [LLM App features](https://github.com/pathwaycom/llm-app) and utilizes the OpenAI API [Embeddings](https://platform.openai.com/docs/api-reference/embeddings) and [Chat Completion](https://platform.openai.com/docs/api-reference/completions) endpoints to generate AI assistant responses.

## Features

- Retrieves the latest weather information from various sources.
- Provides an API interface to explore current weather conditions.
- User-friendly UI with [Streamlit](https://streamlit.io/).
- Filters and presents weather information based on user queries or chosen data sources.
- Supports data and code reusability for offline evaluation.
- Offers the option to use local (cached) or real-time data.
- Extend data sources using Pathway's built-in connectors for JSONLines, CSV, Kafka, Redpanda, Debezium, streaming APIs, and more.

## Upcoming Features

- Incorporate additional data from external APIs, various file formats (Jsonlines, PDF, Doc, HTML, or Text), and databases like PostgreSQL or MySQL.
- Merge data from different sources instantly.
- Maintain a data snapshot to observe variations in weather conditions over time.
- Integrate with BI and analytics tools for downstream processing.
- Set up alerts upon detecting weather shifts.

## Code Sample

```python
import pathway as pw
from common.embedder import embeddings, index_embeddings
from common.prompt import prompt

def run(host, port):
    query, response_writer = pw.io.http.rest_connector(
        host=host,
        port=port,
        schema=QueryInputSchema,
        autocommit_duration_ms=50,
    )

    sales_data = pw.io.jsonlines.read(
        "./examples/data",
        schema=DataInputSchema,
        mode="streaming"
    )

    embedded_data = embeddings(context=sales_data, data_to_embed=sales_data.doc)
    index = index_embeddings(embedded_data)

    embedded_query = embeddings(context=query, data_to_embed=pw.this.query)

    responses = prompt(index, embedded_query, pw.this.query)
    response_writer(responses)

    pw.run()

class DataInputSchema(pw.Schema):
    doc: str

class QueryInputSchema(pw.Schema):
    query: str
```

## Use Case

OpenAI GPT excels at answering questions but may struggle with unfamiliar topics. LLM App efficiently provides context for searches or answers, especially for real-time weather conditions, specific details about weather in a given location, and current atmospheric conditions.

## How the Project Works

1. **Prepare Search Data:**
   - Collect data from chosen sources or upload a CSV file via the UI file-uploader.
   - Map each row into a JSONline schema for better management of large datasets.
   - Chunk documents into short, self-contained sections for embedding.

2. **Embedding and Indexing:**
   - Embed each section using the OpenAI API and retrieve the results.
   - Construct an index on the generated embeddings.

3. **Search (Once per Query):**
   - Generate an embedding for the user's question using the OpenAI API.
   - Retrieve the vector index by relevance to the query.

4. **Ask (Once per Query):**
   - Insert the question and the most relevant sections into a message to GPT.
   - Return GPT's answer.

## How to Run the Project

**Run with Docker:**
- Set environment variables.
- From the project root folder, run `docker compose up` in the terminal.
- Navigate to localhost:8501 in your browser.

**Prerequisites:**
- Ensure Python 3.10 or above is installed.
- Download and install Pip to manage project packages.
- Create an OpenAI account and generate a new API Key.

For more detailed instructions, refer to the [documentation](https://github.com/aryan0931/chatgpt-api-weather-app).

Feel free to explore, contribute, and enhance this weather information API!

https://github.com/aryan0931/chatgpt-api-weather-app/assets/141573833/5e198075-38a4-4acf-9f1f-6e308b0e8b1c

