# Used to work with JSON data
import json

# Used to generate unique IDs
import uuid

# AWS SDK for Python (used to talk to DynamoDB)
import boto3

# Used to read environment variables
import os


# Create DynamoDB service object
dynamodb = boto3.resource("dynamodb")

# Get table name from environment variable set by CDK
table = dynamodb.Table(os.environ["TABLE_NAME"])


def main(event, context):
    # Check HTTP method (GET, POST, etc.)
    # For now, we ONLY handle POST

    method = event.get("httpMethod")
    if method == "POST":
        body = json.loads(event["body"])

        # Create a task item
        item = {
            # Unique ID for each task
            "task_id": str(uuid.uuid4()),

            # Required field from request
            "title": body["title"],

            # Optional field, default = general
            "category": body.get("category", "general"),

            # Default status
            "status": "pending"
        }

        # Save item into DynamoDB table
        table.put_item(Item=item)

        # Send response back to client
        return {
            "statusCode": 201,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps(item)
        }
    
    else:
        return {
                "statusCode": 200,
                "body": "OK"
            }
