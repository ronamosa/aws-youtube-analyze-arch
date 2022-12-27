import json
import scrapetube
import boto3

def lambda_handler(event, context):
    # Get the channel_id from the event
    channel_id = event['channel_id']
    
    # Connect to DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Videos')
    
    # Connect to SQS queue
    sqs = boto3.client("sqs")
    
    # Set the filter expression to match the channel_id attribute
    filter_expression = "channel_id = :val"
    expression_attribute_values = {":val": channel_id}
    
    # Query the Videos table for items with the specified channel_id
    response = table.query(
        IndexName="channel_id-index",
        KeyConditionExpression=filter_expression,
        ExpressionAttributeValues=expression_attribute_values
    )
    
    # Iterate over response and send message to SQS to process
    items = response["Items"]
    
    for item in items:
        message_body = {"video_id": item["video_id"], "channel_id": item["channel_id"]}
        print(message_body)
        sqs.send_message(
            QueueUrl = "https://sqs.ap-southeast-2.amazonaws.com/833580871776/VideoQueue.fifo",
            MessageBody=str(message_body),
            MessageGroupId=channel_id
        )
    
    return "OK"
