# 買い物の支払い金額を求める
# 値段
bear_p = 200
side_p = 100
chiken_p = 100
# 個数
bear_v = 2
side_v = 1
chiken_v = 2
# 割引率
rate = 0.2
# ポイント割引
point = 150
# 計算
payment = chiken_p * (1 - rate)
sum_v = (bear_p * bear_v) + (side_p * side_v) + payment * chiken_v
# 結果を表示
print("買い物の合計は", sum_v, "円")
