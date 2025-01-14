#!/bin/bash
# This script is used to run the python ETL script
cd data/
python3 get_data.py
echo "Python ETL script ran successfully"
sleep 5
python3 clean_data.py
echo 'clean_data.py ran successfully'