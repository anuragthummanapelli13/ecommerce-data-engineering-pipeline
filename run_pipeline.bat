@echo off

cd /d C:\Users\thumm\OneDrive\Desktop\ecommerce-data-engineering-pipeline

call venv\Scripts\activate

python scripts/main_pipeline.py

pause