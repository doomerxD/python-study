import anthropic
import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv("CLAUDE_API_KEY")
)

message = client.messages.create(
    model="claude-3-haiku-20240307", 
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "スクワット102.5kg 3セット×5回 RPE8 でクリアしました。前回は100kgでした。フィードバックをください。"
        }
    ]
)

print(message.content[0].text)