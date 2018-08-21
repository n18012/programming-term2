from Crypto.Cipher import AES
import base64

# 暗号化したいデータとパスワードを指定
message = "自分がしてほしいと思うことを人にもするように"
password = "qwerty"  # 適当なパスワードを指定
iv = "L3f4mITJtCIPV9af"  # 初期化ベクトル（16文字で適当な値を指定）
mode = AES.MODE_CBC

# 特定の長さの倍数にするため空白でデータを埋める関数
def mkpad(s, size):
    s = s.encode("utf-8")
    pad = b' ' * (size - len(s) % size)  #
    return s + pad

# 暗号化する
def encrypt(password, data):
    # 特定の長さに調整する
    password = mkpad(password, 16)  # 16の倍数に揃える
    data = mkpad(data, 16)  # バイト列に変換し16の倍数に揃える
    password = password[:16]
    # 暗号化
    aes = AES.new(password, mode, iv)
    data_cipher = aes.encrypt(data)
    return base64.b64encode(data_cipher).decode("utf-8")

# 復号化する
def decrypt(password, encdata):
    # パスワードの文字列を調整
    password = mkpad(password, 16)  # 16の倍数に揃える
    password = password[:16]  # ちょうど16文字に揃える
    # 複合化
    aes = AES.new(password, mode, iv)
    encdata = base64.b64decode(encdata)
    data = aes.decrypt(encdata)
    return data.decode("utf-8")


# 暗号化する
enc = encrypt(password, message)
# 複合化する
dec = decrypt(password, enc)

# 結果を表示する
print("暗号化:", enc)
print("復号化:", dec)
