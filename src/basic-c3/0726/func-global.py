# 関数の外でvalueに100を代入
value = 100

def changeValue():
    """
    valueの値を変更

    Parameters
    ----------
    なし

    Returns
    -------
    なし
    """
    # valueをグローバル宣言
    global value
    # 関数の内側でvalueを変更
    value = 20

changeValue()
print("value=", value)