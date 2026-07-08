# Paid Media ETL Project

---
## Overview

The pipeline ingests raw paid media export data, cleans and standardizes the data, applies data quality checks, removes duplicates, and produces an analytics-ready dataset at campaign daily grain.

---
## Pipeline flow:

Raw CSV → Ingestion → Cleaning → Transformation → Aggregation → Batch Aggregation → Parquet Output → Validations → Analysis

---
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

- **python main.py**
  - Main pipeline script responsible for data ingestion, cleaning, transformations, and generating the final cleaned output file.

- **python src/validations_checks_menu.py**
  - Interactive validation script that allows users to select and run specific data quality checks.

- **python src/analysis_menu.py**
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
## Design Decisions

- **Chunk-Based Processing**
  - The source CSV is processed in chunks instead of being loaded entirely into memory. This keeps memory usage low and allows the pipeline to handle datasets much larger than the available RAM.

- **Recursive Chunk Aggregation**
  - Intermediate chunk results are recursively aggregated into larger batches until a single final dataset is produced. This approach avoids loading all intermediate files simultaneously while maintaining scalability.

- **Modular Architecture**
  - The pipeline is divided into ingestion, transformations, validation, analysis, and output generation modules, making the code easier to maintain, test, and extend.

- **Parquet Output**
  - The cleaned dataset is stored in Parquet format, providing efficient compression, faster analytical queries, and reduced storage requirements compared to CSV.

- **Data Quality First**
  - Validation checks are performed before analysis to ensure that business insights are generated from clean and reliable data.

---
## Project Walkthrough

1. The raw CSV file is read using chunk-based processing.
2. Each chunk is cleaned, transformed, and saved as an intermediate Parquet file.
3. The intermediate chunks are recursively aggregated into larger batches until a single cleaned dataset is produced.
4. Data quality checks are executed against the final dataset.
5. Business analyses are performed on the cleaned data.
6. The final outputs are displayed for reporting and validation.

During development, memory usage was continuously monitored and remained below **500 MB**, well within the assignment's **4 GB memory constraint**. This demonstrates that the chunking and recursive aggregation approach is efficient and scalable for significantly larger datasets (e.g., 3–5 GB files).

For substantially larger datasets or production-scale workloads, I would transition to a distributed processing framework such as **PySpark**, which is designed to process data across multiple cores or machines while maintaining the same processing principles.

---
## Data Transformations
- **date**
  - Trimmed whitespace
  - Converted to datetime format
  - Removed invalid and future dates
  - Standardized format to `YYYY-MM-DD`

- **platform**
  - Trimmed whitespace
  - Converted values to lowercase
  - Standardized separators (`-`, `_`)
  - Normalized platform names (`facebook` → `meta`, `google ads` → `google_ads`)
  - Removed invalid values

- **account_id**
  - Trimmed whitespace
  - Removed extra spaces
  - Removed missing values

- **campaign_id**
  - Trimmed whitespace
  - Removed extra spaces
  - Removed missing values

- **campaign_name**
  - Trimmed whitespace
  - Converted values to lowercase
  - Normalized spacing
  - Filled missing values with `UNKNOWN`

- **impressions**
  - Removed commas
  - Converted values to numeric type
  - Removed missing and negative values
  - Ensured integer values

- **clicks**
  - Removed commas
  - Converted values to numeric type
  - Removed missing and negative values
  - Ensured integer values

- **spend**
  - Removed commas
  - Converted values to numeric type
  - Removed missing and negative values
  - Rounded values to 2 decimal places

- **currency**
  - Trimmed whitespace
  - Converted values to uppercase
  - Normalized currency names (`EURO` → `EUR`)
  - Filled missing values with `UNKNOWN`

- **conversions**
  - Trimmed whitespace
  - Converted values to numeric type
  - Replaced missing values with `0`
  - Removed negative values

- **video_views**
  - Trimmed whitespace
  - Converted values to numeric type
  - Replaced missing values with `0`
  - Removed negative values

```
These transformations follow standard Data Engineering practices. Final rules should be aligned with the company's data model and business requirements.
```

---
## Data Quality Checks

### Implemented checks:
- **Target Grain Null Validation**
  - Ensures that the target grain columns (`date`, `platform`, `account_id`, and `campaign_id`) do not contain missing values.

- **Schema Validation**
  - Verifies that all required columns are present before processing begins.

- **Target Grain Duplicate Validation**
  - Detects duplicate records based on the target grain (`date`, `platform`, `account_id`, and `campaign_id`).

- **Date Validity Validation**
  - Checks for invalid date formats and ensures that no future dates exist in the dataset.

- **Numeric Metrics Validation**
  - Ensures that numeric metrics (`impressions`, `clicks`, `spend`, `conversions`, and `video_views`) do not contain negative values.

- **Platform Validation**
  - Confirms that all platform values are standardized and belong only to the supported values (`meta` and `google_ads`).

- **Row Count Monitoring**
  - Compares the number of rows before and after processing to monitor records removed during the data cleaning process.

---
## Business Analysis
- **Total Spend by Platform**
  - Calculates the total advertising spend for each platform to compare overall investment.

- **Top 5 Campaigns by Spend**
  - Identifies the five campaigns with the highest total advertising spend.

- **Spend Trend Over Time for One Account**
  - Shows how advertising spend changes over time for a selected account.

- **Average Daily Spend by Platform**
  - Calculates the average daily spend for each platform based on total spend and the number of active days.

- **Campaigns Using USD Currency**
  - Lists campaigns using the `USD` currency along with their total advertising spend.

---
## Author
**Stefan Janicijevic**  
Data Engineer















