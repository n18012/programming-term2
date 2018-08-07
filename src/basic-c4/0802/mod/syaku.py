# 尺からcmへの単位変換
def syaku_to_cm(syaku):
    """
    尺からcmに変換する関数を定義

    Parameter
    ---------
    syaku : int or float
        尺の値

    Returns
    -------
    cmの値
    """
    return round(syaku * 30.303, 3)
print(__name__)
if __name__ == '__main__':
    print(syaku_to_cm(30))
