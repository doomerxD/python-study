import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('WorkoutRecords')

# 特定のユーザーの全記録を取得
response = table.query(
    KeyConditionExpression='user_id = :user_id',
    ExpressionAttributeValues={
        ':user_id': 'yusuke'
    }
)

# 取得したデータを表示
for item in response['Items']:
    print(item)