- Install aws-shell
```
pip install aws-shell
```


- Configure
```
aws configure

->1st I have to run the install part though -> 2nd I put my credentials
```


The path road for the App
```
cd C:\Users\steli\Desktop\AwsApp-Rekognition-Vog

```


- Create a collection on aws rekognition
```
aws rekognition create-collection --collection-id facerecognition_collection --region us-east-1
```


- Create table on DynamoDB
```
aws dynamodb create-table --table-name face_recognition --attribute-definitions AttributeName=RekognitionId,AttributeType=S --key-schema AttributeName=RekognitionId,KeyType=HASH --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 --region us-east-1
```


- Create S3 bucket
```
aws s3 mb s3://bucket-name --region us-east-1
```



The path road to run the script
```
cd C:\Users\steli\Desktop\AwsApp-Rekognition-Vog\App-Test 

If i make any change to where the folder is located i need to fix that!
```


-Call the App-Test Python script
```
python .\Face-Test.py

Need to call it every time after using it -> Cause it returns back to default mode.
From the correct path!
```