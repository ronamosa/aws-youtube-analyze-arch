import boto3
import scrapetube
from datetime import datetime

def lambda_handler(event, context):
    # Extract the channel information from the event data
    channel_id = event['channel_id']
    name = event['name']
    description = event['description']

    # Date
    today = datetime.today()
    
    # Create a DynamoDB client
    dynamodb = boto3.client('dynamodb')

    # Create a new channel
    channel = {
        'channel_id': { 'S': channel_id },
        'name': { 'S': name },
        'description': { 'S': description },
    }

    # Insert the new channel into the table
    dynamodb.put_item(TableName='Channels', Item=channel)