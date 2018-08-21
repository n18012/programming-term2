# パッケージをインポート
import qrcode
# QRコードを生成
img = qrcode.make("https://www.youtube.com/")
# ファイルに保存
img.save("qrcode-test.png")
