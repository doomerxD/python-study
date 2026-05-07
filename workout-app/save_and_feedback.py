import boto3
import anthropic
import os
from decimal import Decimal
from dotenv import load_dotenv
from datetime import datetime

# 環境変数読み込み
load_dotenv()

# AWS DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('WorkoutRecords')

# Claude API
claude_client = anthropic.Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))

# 今日のトレーニング記録を入力
print("=== トレーニング記録入力 ===")
exercise = input("種目名: ")
weight = Decimal(input("重量(kg): "))
sets = int(input("セット数: "))
reps = int(input("回数: "))
rpe = int(input("RPE: "))

# DynamoDBに保存
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
table.put_item(
    Item={
        'user_id': 'yusuke',
        'timestamp': timestamp,
        'exercise': exercise,
        'weight': weight,
        'sets': sets,
        'reps': reps,
        'rpe': rpe
    }
)
print(f"\n✅ 記録を保存しました（{timestamp}）\n")

# 過去の記録を取得
response = table.query(
    KeyConditionExpression='user_id = :user_id',
    ExpressionAttributeValues={':user_id': 'yusuke'}
)
records = sorted(response['Items'], key=lambda x: x['timestamp'], reverse=True)

# Claude にフィードバック生成を依頼
if len(records) >= 2:
    latest = records[0]
    previous = records[1]
    
    prompt = f"""
あなたはパーソナルトレーナーです。以下のトレーニング記録にフィードバックをください。

【今回】
種目: {latest['exercise']}
重量: {latest['weight']}kg
セット×回数: {latest['sets']}×{latest['reps']}
RPE: {latest['rpe']}

【前回】
重量: {previous['weight']}kg
セット×回数: {previous['sets']}×{previous['reps']}
RPE: {previous['rpe']}

短く、トレーニングの総評と次回の提案をお願いします。
"""
    
    message = claude_client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}]
    )
    
    print("=== Claude からのフィードバック ===")
    print(message.content[0].text)
else:
    print("前回のデータがないため、フィードバックは生成されませんでした。")