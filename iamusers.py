import boto3
import sys

access_key=sys.argv[0]
secret_key=sys.argv[1]
client = boto3.client('iam',aws_access_key_id=access_key, aws_secret_access_key=secret_key)

listusrs = client.list_users()

for i in listusrs['Users']:
    for k in i.keys():
        print(k,":", i[k])
