import random
goal = 10
cur_x = []
def shake_dice():
    """
    サイコロを振る関数

    Parameters
    ----------
    なし

    Returns
    -------
    random.randint(1, 6)
    """
    return random.randint(1, 6)

def go_forward(Advance_forward):
    """
    リストの合計

    Parameters
    ----------
    Advance_forward : リスト[]
    リスト名を入れる

    Returns
    -------
    sum関数で合計した値
    """
return sum(Advance_forward)

while True:
    user = input("サイコロを振って下さい")
    if user == "":
        result = shake_dice
        cur_x.appends(result)
        if go_forward(cur_x) >= goal:
            print('{}がでました。ゴールです。おめでとうございます。'.format(result))
            exit()
        else:
            print('{}がでました。現在位置は{}です。'.format(result, go_forward(cur_x)))
    else:
       print("サイコロを振るにはenterを押して下さい")
