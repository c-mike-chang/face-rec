import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('image01.jpeg','Malathi Veeraraghavan'),
      ('image02.jpeg','Malathi Veeraraghavan'),
      ('image03.jpeg','Malathi Veeraraghavan'),
      ('image04.jpeg','Lu Feng'),
      ('image05.jpeg','Lu Feng'),
      ('image06.jpeg','Lu Feng'),
      ('image07.jpeg','Mark Sherriff'),
      ('image08.jpeg','Mark Sherriff'),
      ('image09.jpeg','Mark Sherriff')
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('cmc8dm','index/'+ image[0])
    ret = object.put(Body=file, Metadata={'FullName':image[1]})
