import openai
import dotenv
import os

# APIキーの設定
dotenv.load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")

# メッセージを作成
messages = [
  {
    "role":"system",
    "content":"あなたは端的に発言するAIです。"
  },
  {
    "role":"user",
    "content":"こんにちは"
  }
]

# API呼び出し
res = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=messages,
)

# 結果を出力
print(res["choices"][0]["message"]["content"])