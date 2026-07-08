from src.ingestion import process_ingestion_chunks
from src.aggregate_chunks import batch_aggregation
from src.generating_output import generating_output

ingestion_time = process_ingestion_chunks()
batch_time = batch_aggregation()
output_time = generating_output()

total_time = ingestion_time + batch_time + output_time

print("***********************")
print(f"Ingestion Time: {ingestion_time:.2f} seconds")
print(f"Batch Aggregation Time: {batch_time:.2f} seconds")
print(f"Output Generation Time: {output_time:.2f} seconds")
print(f"Total Pipeline Time: {total_time:.2f} seconds")