n = int(input())
scores = {"太郎の得点":0, "花子の得点":0}

for i in range(n):
    taro_str, hanako_str = input().split()
    
    if taro_str > hanako_str:
        scores["太郎の得点"] += 3
    elif taro_str == hanako_str:
        scores["太郎の得点"] += 1
        scores["花子の得点"] += 1
    else:
        scores["花子の得点"] += 3

print(f"{scores['太郎の得点']} {scores['花子の得点']}")     #ダブルクォーテーションの重複を避ける