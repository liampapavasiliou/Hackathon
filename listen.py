import subprocess
import json
import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv
import os
import time
import retrive
import rekognition

def process(files):
    with open("/home/liam/Hackathon/events/race.txt", "r") as file:
        data=file.read().split("\n");
    for i in files:
        rekognition.rek("staging"+i.decode("utf-8")) 
        text =retrive.retr(i + '.txt')
        for j in data:
            for l in text:
                if(l in j):
                    os.system("mv " + i + " /home/liam/Hackathon/events/"+j)
        os.system("rm "+ i)

while True:
    files = subprocess.check_output(["ls", "staging"])
    time.sleep(0.5)
    if files != "":
        process(files.split())

