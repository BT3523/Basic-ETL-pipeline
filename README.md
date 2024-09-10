# Basic-ETL-pipeline

ETL Pipeline for FilterLists Data
This project implements an ETL (Extract, Transform, Load) pipeline using Python to extract, clean, and load data from the FilterLists public API. The API provides information about filter lists used for ad blockers and privacy tools. The extracted data is transformed into a structured format and stored in an SQLite database for analysis and querying.

Features:
API Integration: Extracts real-time data on over 300+ filter lists using the FilterLists public API.
Data Transformation: Uses pandas to clean and normalize the data, including handling missing values, selecting relevant fields (e.g., name, description, syntax, and viewUrl), and structuring the dataset.
Database Storage: Loads the cleaned data into an SQLite database using SQLAlchemy, storing it in a relational format for easy querying.
Automation: Designed as a reusable pipeline to automatically fetch and process new data with minimal modifications.
Technologies Used:
Python: Core programming language for the ETL pipeline.
requests: For fetching data from the API.
pandas: For data cleaning and transformation.
SQLAlchemy: For interacting with the SQLite database.
SQLite: For structured data storage.
