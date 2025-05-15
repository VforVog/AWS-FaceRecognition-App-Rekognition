---- Brief Explanation - More Structured in the Architecture Folder ----

This is an AWS based Face Recognition App! By using AWS resources, such as 
S3 Bucket, Lambda, IAM, Rekognition and DynamoDB.

We start by conecting to our AWS account using through AWS CLI.
Next, we import and configure the resources using AWS CLI commands (alternatively, you can perform the same actions through the AWS Management Console).

Then we import our Python script to Lambda. Lambda connects with Rekognition under IAM policies (which we created). 

We upload Images to train the Machine Learning of Rekognition. 

Finally we use the python script to run the app!


*P.s.: Location -> US East, N. Virginia

