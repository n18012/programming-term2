# CPUが絶対に勝つじゃんけんプログラム
janken = input("何を出しますか? 1:グー、2:チョキ、3:パー : ")
if janken == 1:
    print("CPUが{a}を出しました。あなたの負けです。".format(a="パー"))
elif janken == 2:
    print("CPUが{b}を出しました。あなたの負けです。".format(b="グー"))
elif janken == 3:
    print("CPUが{c}を出しました。あなたの負けです。".format(c="チョキ"))
else:
    print("入力が不正です。終了します。")
