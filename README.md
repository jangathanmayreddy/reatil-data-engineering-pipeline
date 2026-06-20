# Retail Sales Data Engineering Pipeline

A GitHub-ready data engineering project that demonstrates building a batch data pipeline for retail sales analytics using Python, SQL, data quality checks, and workflow orchestration.

This project is designed for a Data Engineer with around 4 years of experience and shows practical skills in ETL/ELT, data validation, dimensional modeling, pipeline automation, and production-style documentation.

## Business Problem

Retail leadership wants a trusted daily sales analytics layer to track revenue, orders, customer activity, product performance, and regional trends. Raw order, customer, and product data arrives daily as CSV files. The goal is to clean, validate, transform, and load the data into analytics-ready tables.

## Architecture

Raw CSV files → Python ingestion → Data quality checks → Cleaned staging data → SQL transformations → Star schema analytics tables → BI-ready outputs

## Tech Stack

- Python
- Pandas
- SQL
- SQLite for local warehouse simulation
- Pytest
- GitHub Actions
- Modular ETL design

## Project Structure

```text
retail-data-engineering-pipeline/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── config.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── data_quality.py
│   └── main.py
├── sql/
│   └── models/
│       ├── dim_customers.sql
│       ├── dim_products.sql
│       └── fact_sales.sql
├── pipelines/
│   └── daily_sales_pipeline.py
├── tests/
│   └── test_data_quality.py
├── docs/
│   └── data_model.md
├── .github/workflows/
│   └── ci.yml
├── requirements.txt
└── README.md
```

## Features

- Ingests raw customer, product, and order data
- Performs schema checks, null checks, duplicate checks, and business rule validation
- Cleans and standardizes raw data
- Loads data into a local SQLite warehouse
- Builds dimensional tables and a fact table
- Includes unit tests for data quality rules
- Includes GitHub Actions CI workflow
- Includes documentation for the data model

## How to Run

```bash
pip install -r requirements.txt
python src/main.py
```

Run tests:

```bash
pytest tests/
```

## Sample Analytics Questions Supported

- What is daily revenue by region?
- Which products generate the highest revenue?
- How many unique customers purchased each month?
- What is the average order value?
- Which orders failed data quality checks?

## Resume Bullet Example

Built an end-to-end retail sales data pipeline using Python, SQL, and automated data quality checks to ingest raw order, customer, and product files, transform them into a star schema model, and generate BI-ready sales analytics tables with CI-based validation.
