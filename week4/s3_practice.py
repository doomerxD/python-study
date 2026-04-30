import boto3

# S3クライアントを作る
s3 = boto3.client("s3")

s3.upload_file(
    "/Users/yusukeuekusa/python-study/week4/report.csv",  # ローカルのパス
    "yusuke-practice-2026",   # バケット名
    "report.csv"         # S3上のファイル名
)

response = s3.list_objects_v2(Bucket="yusuke-practice-2026")
for obj in response["Contents"]:
    print(f"{obj['Key']} : {obj['Size']} bytes")


s3.download_file(
    "yusuke-practice-2026",          # どのバケットから
    "report.csv",    # S3のどのファイルを
    "/Users/yusukeuekusa/python-study/week4/downloaded_report.csv"         # ローカルのどこに保存するか
)

with open("/Users/yusukeuekusa/python-study/week4/downloaded_report.csv", "r") as f:
    print(f.read())