import os
import boto3

AWS_ACCESS_KEY_ID = 'AKIAIKJFNWXJ3BJ24ZBA'
AWS_ACCESS_KEY_SECRET = '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'
bucket_name = 'dev.ctzn.co.uk'
sourceDir = "../../docs/build/html/"
destDir = ''

r = boto3.setup_default_session(region_name='eu-west-1')
s3 = boto3.resource('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_ACCESS_KEY_SECRET)
bucket = s3.Bucket(bucket_name)
uploadFileNames = []
# for (sourceDir, dirname, filenames) in os.walk(sourceDir):
# for filename in filenames:
# bucket.put_object(Key=filename, Body=open("{}{}".format(sourceDir, filename), "rb"))
# break

for subdir, dirs, files in os.walk(sourceDir):
    for file in files:
        this_file = "{}/".format(subdir.split('html/', 1)[1])
        if this_file == "/":
            upload_file = file
        else:
            upload_file = "{}{}".format(this_file, file)

        file_type = file.rsplit('.', 1)[1]

        if file_type == "html":
            content_type = 'text/html'
        elif file_type == "css":
            content_type = 'text/css'
        else:
            content_type = 'binary/octet-stream'

        bucket.put_object(Key=upload_file, Body=open("{}/{}".format(subdir, file), "rb"), ContentType=content_type)

