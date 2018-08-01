# 金額のリストを作成
nums = [13600, 14500, 16000, 11111, 11667]
TAX_RATE = 0.08

# map()を使ってリストnumsを計算
tax_price = list(map(lambda x: round(x * TAX_RATE + x, -1), nums))
# 金額を表示
print(tax_price)
