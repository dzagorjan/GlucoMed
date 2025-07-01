import boto3
import os


AWS_REGION = os.getenv("AWS_REGION", "eu-central-1")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", "test")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "test")
DYNAMODB_ENDPOINT_URL = os.getenv("DYNAMODB_ENDPOINT_URL", "http://dynamodb:8000") # for local testing
DYNAMODB_TABLE_NAME = os.getenv("PATIENTS_TABLE", "Patients")

#Intialize boto3 resource



dynamodb = boto3.resource(
    "dynamodb",
    region_name = AWS_REGION,
    aws_access_key_id = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    endpoint_url=DYNAMODB_ENDPOINT_URL
)

table = dynamodb.Table(DYNAMODB_TABLE_NAME)



