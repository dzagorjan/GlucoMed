# create_table.py
import boto3
import os
import time
from botocore.exceptions import ClientError


dynamodb = boto3.resource(
    "dynamodb",
    region_name="eu-central-1",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    endpoint_url="http://dynamodb:8000",    
)


table_name="Readings"
client = dynamodb.meta.client

def wait_for_dynamodb():
    print("Waiting for DynamoDB to be ready...")
    retries = 10
    for attempt in range(retries):
        try:
            client.list_tables()
            print("DynamoDB is ready.")
            return
        except Exception as e:
            print(f"Not ready yet ({attempt+1}/{retries}): {e}")
            time.sleep(2)
    raise RuntimeError("DynamoDB is not ready after waiting.")

def create_readings_table():
    retries = 5
    for attempt in range(retries):
        try:
            existing_tables = client.list_tables()["TableNames"]
            if table_name in existing_tables:
                print(f"Table '{table_name}' already exists.")
                return

            print(f"Creating table '{table_name}'...")
            table = dynamodb.create_table(
                TableName=table_name,
                KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
                AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
                ProvisionedThroughput={
                    "ReadCapacityUnits": 5,
                    "WriteCapacityUnits": 5
        },
                
            )
            table.wait_until_exists()
            print(f"Table '{table_name}' successfully created.")
            return
        except ClientError as e:
            print(f"Attempt {attempt+1}: {e}")
            time.sleep(2)
    raise RuntimeError("Failed to create table after retries.")



if __name__ == "__main__":
    wait_for_dynamodb()
    time.sleep(1)
    create_readings_table()
