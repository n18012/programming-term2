# 買い物の支払い金額を求める
# 値段
beer_p = 200
side_p = 100
chicken_p = 100

# 個数
beer_v = 2
side_v = 1
chicken_v = 2

# 割引率
rate = 0.2
# ポイント割引
point_off = 150

# 計算
chicken_p_off = chicken_p * (1 - rate) * chicken_v
sum_v = (beer_p * beer_v) + (side_p * side_v) + chicken_p_off - point_off
# 結果を表示
print("買い物の合計は", sum_v, "円")
