import boto3
import time
import os

# Set up DynamoDB resource and table
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table_name = os.getenv("DDB_TABLE_NAME", "HybridHealAI_Tasks")  # Use env var or fallback
table = dynamodb.Table(table_name)

def check_for_tasks():
    response = table.scan()
    for item in response.get('Items', []):
        if item.get('status') == 'pending':
            print(f"🔧 Fixing issue: {item['issue_type']}")
            # Example logic to mark task as resolved
            table.update_item(
                Key={'task_id': item['task_id']},
                UpdateExpression="SET #s = :s",
                ExpressionAttributeNames={'#s': 'status'},
                ExpressionAttributeValues={':s': 'resolved'}
            )

if __name__ == '__main__':
    while True:
        check_for_tasks()
        time.sleep(30)

