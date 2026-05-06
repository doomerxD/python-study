import boto3
from decimal import Decimal  # ← これを追加

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('WorkoutRecords')

# 2回目のスクワット記録（前回より2.5kg重い）
table.put_item(
    Item={
        'user_id': 'yusuke',
        'timestamp': '2026-05-08 21:00:00',
        'exercise': 'スクワット',
        'weight': Decimal('102.5'),  # ← Decimal()で囲む
        'sets': 3,
        'reps': 5,
        'rpe': 8
    }
)

print("2回目の記録を保存しました！")