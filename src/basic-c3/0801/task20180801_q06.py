# (人物、身長)のリスト(各要素はタプルで作成)
arasi_list = [
    ("Aiba", 175),
    ("Matsumoto", 172),
    ("Ninomiya", 168),
    ("Oono", 166),
    ("Sakurai", 171),
]

# 伸長順に並び替える
older_list = sorted(
    arasi_list,
    key=lambda arasi: arasi[1]
)

# 結果を表示
for i in older_list: print(i)
