import json
import scrapetube
import boto3

def lambda_handler(event, context):
    channel_id = event['channel_id']
    videos = scrapetube.get_channel(channel_id, sort_by='newest')
    
    # Create a DynamoDB client
    dynamodb = boto3.client('dynamodb')
    
    for video in videos:

        result = {
            'video_id': { 'S': str(video['videoId'])},
            'channel_id': {'S': channel_id },
            'title': {'S': str(video['title']['runs'][0]['text'])},
            'duration': {'S': str(video['lengthText']['simpleText'])},
        }
        
        #print(result)
        
        dynamodb.put_item(TableName='Videos', Item=result)

    return "OK"