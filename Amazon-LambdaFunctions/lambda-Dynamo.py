import boto3
import json
import uuid
from datetime import datetime
from boto3.dynamodb.conditions import Key


def respond(err, response=None):
	return {
		'statusCode': '400' if err else '200',
		'body': err if err else json.dumps(response),
		'headers': {
			'Content-Type': 'application/json',
		},
	}


def lambda_handler(event, context):

	method = event['httpMethod']

	if method not in ['POST']:
		return respond('Lambda function only supports POST request for the moment.')

	try:
		message = event['Message']
		username = event['Username']
		msgID = uuid.uuid4()
	except KeyError:
		return respond('Request is not properly formated.')


	messageTable = boto3.resource('dynamodb').Table('Message')

	#create a new db entry
	messageData = {
		'SentOn': str(datetime.utcnow()),
		'UserID': username,
		'Value': message,
	}

	messageTable.put_item(Item=messageData)

	return respond(None, messageData)
