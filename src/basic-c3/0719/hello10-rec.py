# 再帰関数を定義
def say_hello(i):
    '''
    「ハロー」を指定した回数出力する
    （関数の再帰呼び出しを利用）

    Parameters
    ----------
    i : int
        回数

    Returns
    -------
    なし
    ----
    '''
    if i <= 0:  # iが0になったらreturn
        return
    print("ハロー", i)
    say_hello(i - 1)

# 実行
say_hello(10)
