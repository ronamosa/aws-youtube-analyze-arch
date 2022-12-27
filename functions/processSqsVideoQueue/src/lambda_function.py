import json
import boto3
from youtube_transcript_api import YouTubeTranscriptApi

def lambda_handler(event, context):
    
    # setup clients
    sqs = boto3.client('sqs')
    s3 = boto3.client('s3')
    
    # fetch message from SQS
    queue_url = "https://sqs.ap-southeast-2.amazonaws.com/833580871776/VideoQueue.fifo"
    
    response = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=1)

    if 'Messages' not in response:
        print("Cant find Messages in response. Exiting...")
        return
    
    # Process the response
    json_data = json.dumps(response)
    parsed_data = json.loads(json_data)
    
    # Process the messages
    body = parsed_data['Messages'][0]['Body']
    videoId = body[0]
    
    # Use the YouTube Transcript API to get the transcript of the video
    try:
        transcript = YouTubeTranscriptApi.get_transcript(videoId)
            # Save the response to an S3 bucket
            #bucket_name = 'YOUR_BUCKET_NAME'
            #key = f'{channel_id}/{video_id}/api_response.json'
            #s3.put_object(Bucket=bucket_name, Key=key, Body=api_response)
            
            # Delete the message from the queue
            # receipt_handle = message['ReceiptHandle']
            # sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)
    except Exception as e:
        # Print the exception message
        print(e)
    
    return