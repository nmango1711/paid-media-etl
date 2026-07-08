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

---
## Running the Pipeline

**python main.py**
- Main pipeline script responsible for data ingestion, cleaning, transformations, and generating the final cleaned output file.

**python src/validations_checks_menu.py**
- Interactive validation script that allows users to select and run specific data quality checks.

**python src/analysis_menu.py**
- Interactive analysis script that provides multiple reporting options and allows users to choose which analysis to execute.

---
## Repository Structure
```
paid-media-etl/
│
├── data/                            
│   ├── raw_data/
│       ├── paid_media_export.csv    # Source csv data file
│   ├── batch_chunks/                # Temporary storage for aggregated ingestion chunks
│   ├── cleaned_data/                # Stores cleaned and transformed output data
│   ├── ingestion_chunks/            # Stores intermediate chunks created during ingestion
|
├── src/                               
│   ├── aggregate_chunks.py          # Aggregates processed ingestion chunks
│   ├── analysis_menu.py             # Provides menu options for running analyses
│   ├── analysis.py                  # Performs business analysis on processed data
│   ├── generating_output.py         # Generates final output file
│   ├── ingestion.py                 # Handles data ingestion from source files
│   ├── pipeline.py                  # Orchestrates the complete data pipeline workflow
│   ├── transformations.py           # Cleans and transforms raw data
│   ├── validation_checks.py         # Performs data quality validation checks
│   ├── validation_checks_menu.py    # Provides menu options for validation checks
│
├── venv/                            # Virtual environment
│                          
├── .gitignore                       # gitignore file
│
├── main.py                          # Main pipeline script for ingesting, cleaning, transforming and generating output file 
│
├── README.md                        # README.md file
│
├── requirements.txt                 # File for necessary libraries installation
                                      
```
---
