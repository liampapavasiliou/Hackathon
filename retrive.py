import subprocess
import json
import boto3
from botocore.exceptions import ClientError
import os
from dotenv import load_dotenv

load_dotenv()

# Put your AWS credentials in a .env file
access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

s3_client = boto3.client(
    service_name="s3",
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key,
    region_name="us-west-2",
)


#make name work later
name = "WCCs.jpeg"


response1 = s3_client.download_file(
        "output-hack",
        name+"txt",
        "/home/liam/Hackathon/"+name+".txt"
)

subprocess.run(["cat", name+".txt"])
