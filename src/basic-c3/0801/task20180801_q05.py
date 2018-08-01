# (人物、年齢)のリスト(各要素はタプルで作成)
arasi_list = [
    ("Aiba", 35),
    ("Matsumoto", 34),
    ("Ninomiya", 35),
    ("Oono", 37),
    ("Sakurai", 36),
]

# 年長順に並び替える
older_list = sorted(
    arasi_list,
    key=lambda arasi: arasi[1],
    reverse=True)

# 結果を表示
for i in older_list: print(i)
