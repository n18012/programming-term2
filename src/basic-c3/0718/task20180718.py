# 注文プログラム
# メインメニューを辞書型で定義
menu = {'DripCoffee': 280, 'ColdBrewCoffee': 320, 'CafeLatte': 330, 'SoyLatte': 380, 'Cappuccino': 330, 'CaramelFrappuccino': 470, 'MacchaCreamFrappuccino': 470}

# オプションを辞書型で定義
option = {'LowFatMilk': 0, 'NonFatMilk': 0, 'SoyMilk': 50, 'DeepCoffee': 60, 'WhipCream': 70, 'CaramelShrup': 60, 'ChocoSource': 0, 'DeCafe': 50}

# 注文内容のリスト
naiyo = []
# メニューを入力
while True:
    name = input("メインメニューを選んで下さい :")
    if name == "" or name == "q":
        print("キャンセルされました")
        exit()
    if name == menu:
        print("メインメニューを承りました。")
    else:
        print("選択されたメニューはありません")
# 合計金額

