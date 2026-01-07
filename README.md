<br>
<p align="center">
  <b> 🚀 AWS Face Recognition App </b>
</p>
<br>
  
An end-to-end Face Recognition application built using AWS services like Rekognition, S3, Lambda, IAM, and DynamoDB.
This project demonstrates how to leverage serverless and AI/ML services on AWS to build a scalable image recognition pipeline.
<br><hr>

<b> ⚡ Features </b>

- Upload images to an S3 bucket for processing.

- Lambda function triggers AWS Rekognition for facial analysis.

- Results (faces detected, attributes, confidence scores) are stored in DynamoDB.

- IAM policies ensure secure service-to-service communication.

- Fully serverless and scalable — no servers to manage.

  <br>

<b>🛠️ Technologies Used</b>

- Amazon S3 – Image storage

- AWS Lambda – Serverless compute

- Amazon Rekognition – Face detection & recognition 

- Amazon DynamoDB – NoSQL database for results

- AWS IAM – Secure role & policy management

- AWS CLI & Python – Infrastructure setup & scripting
<br>
<b> 🚀 How It Works </b>

- Setup: Connect to your AWS account using the AWS CLI.

- Provision Resources: Create S3, DynamoDB, and IAM roles using CLI or the AWS Console.

- Deploy Code: Upload the Python script to AWS Lambda.

- Upload Images: Train Rekognition by uploading images to S3.

- Run Inference: Lambda triggers Rekognition to detect and analyze faces.
<br>

<b>📍 Deployment Details</b>

Region: US East (N. Virginia) - us-east-1

---

Simulation <br>
<br>
![Demo](gif/gif.gif)
