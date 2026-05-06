import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('WorkoutRecords')

# スクワットの記録を全部取得
response = table.query(
    KeyConditionExpression='user_id = :user_id',
    ExpressionAttributeValues={
        ':user_id': 'yusuke'
    }
)

# timestampで新しい順にソート
records = sorted(response['Items'], key=lambda x: x['timestamp'], reverse=True)

# 最新の記録
latest = records[0]
print(f"【最新記録】{latest['timestamp']}")
print(f"種目：{latest['exercise']}")
print(f"重量：{latest['weight']}kg")
print(f"セット×回数：{latest['sets']}×{latest['reps']}")
print()

# 前回の記録と比較
if len(records) >= 2:
    previous = records[1]
    diff = latest['weight'] - previous['weight']
    print(f"【前回との比較】")
    print(f"前回：{previous['weight']}kg")
    print(f"今回：{latest['weight']}kg")
    print(f"差分：+{diff}kg 👏")
else:
    print("前回のデータがありません")

# 次回の提案
print()
print("【次回の提案】")

if latest['rpe'] <= 8:
    next_weight = latest['weight'] + Decimal('2.5')
    print(f"RPE {latest['rpe']}でクリアできたので、次回は{next_weight}kgに挑戦しましょう！")
elif latest['rpe'] == 9:
    next_weight = latest['weight']
    print(f"RPE 9だったので、次回も{next_weight}kgで様子を見ましょう。")
else:
    next_weight = latest['weight'] - Decimal('2.5')
    print(f"RPE 10は重すぎました。次回は{next_weight}kgに下げましょう。")

print(f"推奨セット×回数：{latest['sets']}×{latest['reps']}")