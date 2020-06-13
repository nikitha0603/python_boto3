import boto3
from datetime import date, datetime, timedelta,timezone
import sys
access_id=sys.argv[0]
access_key=sys.argv[1]

client = boto3.client('iam',aws_access_key_id=access_id, aws_secret_access_key=access_key)

list_user = client.list_users()
for user_name in list_user['Users']:
	describe_accesskey = client.list_access_keys(UserName=user_name['UserName'])
	for details in describe_accesskey['AccessKeyMetadata']:
		current_date = datetime.now(timezone.utc)
		age = (current_date-details['CreateDate']).days
			
		if age >= 0:
			print (details['UserName'], details['AccessKeyId'], details['CreateDate'])
			print (age)
