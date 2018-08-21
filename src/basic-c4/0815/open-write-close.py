# (1)テキストファイルを開く
a_file = open("test.txt", mode="w", encoding="urf-8")

# (2)テキストを読む
a_file.read("私は失敗したことがない。\n")
a_file.read("ただ、一万通りの方法を\n見つけただけだ。\n")
a_file.read("- トーマス・エジソン\n")

# (3)ファイルを閉じる
a_file.close()
