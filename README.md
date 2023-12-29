# ChatGPT Python API for Weather Information

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



ChatGPT
Certainly! Below is a modified version of the readme file for a weather application:

markdown
Copy code
# ChatGPT Python API for Weather Information

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

## Demo

In case you use OpenWeatherMap API as a data source for the project, it provides real-time weather information for various locations.
When the user has the following query in the API request:

```text
What is the weather like in New York today?
You will get the response with current weather details for New York:

LLM App responds with weather information from OpenWeatherMap

As evident, ChatGPT interface offers specific information about the current weather conditions.

Code sample

It requires only a few lines of code to build a real-time AI-enabled data pipeline:



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
