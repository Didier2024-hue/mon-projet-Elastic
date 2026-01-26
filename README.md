🔍 Elasticsearch – Search & Analytics Evaluation Project

DataScientest | Data Engineering / Search Architecture

🎯 Context & Objective

This project was completed as part of a technical Elasticsearch assessment at DataScientest.
It simulates a real e-commerce client case in the women’s fashion sector who wants to:

evaluate product relevance,

analyze customer reviews,

perform efficient text and analytical search,

build actionable indicators using Kibana.

The objective is to demonstrate operational mastery of Elasticsearch, from data ingestion to advanced analysis and visualization.

🧠 Data Engineer / Search Architect Approach

The project follows a distributed search engine logic:

Structured data ingestion (CSV)

Definition of a consistent mapping

Data exploration and quality checks

Statistical analysis and aggregations

Advanced decision-oriented queries

Kibana visualizations

Although the dataset is small, the project is designed to be scalable and aligned with production Elasticsearch architectures.

📦 Deliverable Structure


1️⃣ bulk_script.py – Ingestion & Indexing

This script allows you to:

download the dataset:
https://dst-de.s3.eu-west-3.amazonaws.com/elasticsearch_fr/datasets/Womens_Clothing.csv

create the eval index

define an explicit mapping

ingest the data into Elasticsearch

🎯 Goal: simulate a controlled ingestion pipeline, the foundation of any performant search engine.

2️⃣ eval_elastic_x_y.py Scripts – Evaluation Queries

Each script corresponds to a specific question from the assessment.

Examples of execution:

python3 eval_elastic_1_1.py
python3 eval_elastic_2_3.py


Each run automatically generates a folder for the evaluator:

/eval/questions/q_1-1/
├── mapping.json
├── request.json
├── response.json


mapping.json: index structure

request.json: Elasticsearch query

response.json: raw cluster response

🎯 Goal: ensure traceability, auditability, and reproducibility of analysis.

3️⃣ Data Quality & Exploration

Queries cover:

unique values (Division Name, Department Name, Class Name)

total number of products

consistency between Division and Department

detection of null values

🎯 Goal: understand and ensure data reliability before advanced analysis.

4️⃣ Statistical Analysis & Aggregations

Implemented:

histograms (customer age)

descriptive statistics (average, median ratings)

aggregations by product class

cross-analysis of age vs. product category

🎯 Goal: use Elasticsearch as a real-time analytics engine, not just a text search engine.

5️⃣ Advanced Decision-Oriented Analysis

This section answers business questions such as:

most common terms in highly rated products

most common terms in low-rated products

products the client should prioritize keeping in the catalog

products the client should stop investing in

🎯 Goal: turn data into actionable recommendations for the client.

6️⃣ dashboard.png – Kibana Visualizations

4 visualizations integrated into a Kibana dashboard

Demonstrates ability to industrialize analysis with a real-time BI tool

A deliverable similar to what a client would expect

7️⃣ Informative Files

create_index_eval.txt: index mapping and creation details

verification_index_eval.txt: index existence and consistency verification

🏗️ Target Architecture (Production Projection)

This project is designed to scale toward:

automated ingestion with Logstash / Beats

distributed pipelines

large data volumes (millions of documents)

monitoring and observability in Elasticsearch

🧩 Skills Demonstrated

🔍 Elasticsearch (index, mapping, query DSL)

🐍 Python & Elasticsearch client

📊 Advanced aggregations and statistics

🧠 Business-oriented text analysis

📈 Kibana (dashboards & visualizations)

🏗️ Search & analytics architecture

📁 Professional deliverable structuring
