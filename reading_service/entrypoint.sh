#!/bin/bash 

echo "Waiting DynamoDB..."
until curl -s http://dynamodb:8000 > /dev/null; do
  echo "DynamoDB not ready, waiting..."
  sleep 2
done

echo "Running create_table.py..."
python create_table.py

echo "Running reading-service app..."
exec python -m uvicorn main:app --host 0.0.0.0 --port 8003