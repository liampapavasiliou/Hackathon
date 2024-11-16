import boto3
from botocore.exceptions import ClientError
import os
from dotenv import load_dotenv

load_dotenv()

# Put your AWS credentials in a .env file
access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

client = boto3.client(
    service_name="s3",
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key,
    region_name="us-west-2",
)

response = client.upload_file(
    "/home/liam/WCCs.jpeg",
    "pictures-hack",
    "WCCs.jpeg"
)
