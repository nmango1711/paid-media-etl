# Paid Media ETL Project

---
## Overview

The pipeline ingests raw paid media export data, cleans and standardizes the data, applies data quality checks, removes duplicates, and produces an analytics-ready dataset at campaign daily grain.

---
## Pipeline flow:

Raw CSV → Ingestion → Cleaning → Transformation → Aggregation → Batch Aggregation → Parquet Output → Validations → Analysis

## Requirements

- Python 3.10+
- pandas
- pyarrow

---
## Installation

1. **Clone repository:** git clone https://github.com/nmango1711/paid-media-etl.git
2. **Navigate to the root of the project:** cd paid-media-etl
3. **Create virtual environment:** python -m venv venv
4. **Activate virtual environment:** source venv/bin/activate
5. **Install libraries from requrenments.txt:** pip install -r requirements.txt 
6. **From root of the project create folders and put source csv data in it**: /data/raw_data/paid_media_export.csv                 

## Running the Pipeline

**python main.py**
- Main pipeline script responsible for data ingestion, cleaning, transformations, and generating the final cleaned output file.

**python src/validations_checks_menu.py**
- Interactive validation script that allows users to select and run specific data quality checks.

**python src/analysis_menu.py**
- Interactive analysis script that provides multiple reporting options and allows users to choose which analysis to execute.
