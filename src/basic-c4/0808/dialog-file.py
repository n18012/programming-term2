# ダイアログを表示するために必要なモジュール
import tkinter.filedialog as fd

# ファイル選択ダイアログを表示する
path = fd.askopenfilename(
    title="処理対象のファイルを指定して下さい"  # ダイアログ上部のタイトルを設定
)
print(path)
