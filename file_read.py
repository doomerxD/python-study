import csv

def judge_score(score):
    if score >= 80:
        return "優"
    elif score >= 70:
        return "良"
    elif score >= 50:
        return "可"
    else:
        return "不可"


#問題7
try:
    with open("scores.csv", "r", encoding="UTF-8") as f:
        reader = csv.DictReader(f)
        for line in reader:
            print(f"{line['name']}:{line['score']}点→{judge_score(int(line['score']))}")

except FileNotFoundError:
    print("ファイルが見つかりませんでした")

finally:
    print("問題7処理終了")
