# ダイアログを表示するために必要なモジュール
import tkinter.messagebox as mb

# ダイアログを表示
ans = mb.askyesno("質問", "ラーメンは好きですか？")
if ans:
    # OKボタンがあるだけのダイアログを表示
    mb.showinfo("同意", "僕も好きです。")
else:
    mb.showinfo("本当？", "まさか、ラーメン嫌いだなんて！")
