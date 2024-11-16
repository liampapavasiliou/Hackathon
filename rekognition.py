import json
import boto3
from botocore.exceptions import ClientError
import os
from dotenv import load_dotenv

load_dotenv()

# Put your AWS credentials in a .env file
access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

s3_client = boto3.resource(
    "s3",
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key,
    region_name="us-west-2",
)

rek_client = boto3.client(
    service_name="rekognition",
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key,
    region_name="us-west-2",
)

#make name work later
name = "WCCs.jpeg"
outname = name.split(".")[0] +".txt"
response = rek_client.detect_text (
        Image={"S3Object":{"Bucket":"pictures-hack", "Name":name}}
        )
textDetections = response["TextDetections"]

file = open(outname , "w")

output =""

for text in textDetections:
        output+= ('Detected text:' + text['DetectedText'])
        output+=("\n")
        output+= ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
        output+=("\n")

s3_client.Object("output-hack", outname).put(Body=output)

