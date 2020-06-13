import boto3
from datetime import date, datetime, timedelta,timezone

client = boto3.client('iam',aws_access_key_id="AKIATKQXWGYZORI4MN5K", aws_secret_access_key="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")

list_user = client.list_users()
for user_name in list_user['Users']:
	describe_accesskey = client.list_access_keys(UserName=user_name['UserName'])
	for details in describe_accesskey['AccessKeyMetadata']:
		current_date = datetime.now(timezone.utc)
		age = (current_date-details['CreateDate']).days
			
		if age >= 0:
			print (details['UserName'], details['AccessKeyId'], details['CreateDate'])
			print (age)