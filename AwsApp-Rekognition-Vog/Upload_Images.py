import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('image1.jpg','Pope Vatican'),
      ('image2.jpg','Pope Vatican'),
      ('image3.jpg','Kyriakos Mitsotakis'),
      ('image4.jpg','Kyriakos Mitsotakis'),
      ('image5.jpg','Ioannis Antetokoumpo'),
      ('image6.jpg','Ioannis Antetokoumpo')
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('vogapp-facerecognition','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})
