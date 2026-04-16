def judge_score(score):
    if score >= 95:
        return "優"
    elif score >= 70:
        return "良"
    elif score >= 50:
        return "可"
    else:
        return "不可"

scores = [95, 72, 55, 40, 88]

for score in scores:
    result = judge_score(score)
    print(f"{score}点 → {result}")
