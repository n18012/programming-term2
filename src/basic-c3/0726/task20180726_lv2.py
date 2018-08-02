import random
goal = 10

# ランダムに入ってきた整数
cur_x = []

# サイコロを振る関数を定義
def shake_dice():
    '''
    ランダムなサイコロを振る関数

    parameters
    ----------
    なし

    Return
    ------
    random.randint(1, 6)
    １から６までのランダムな整数
    '''
    return random.randint(1, 6)

# 前に進む関数を定義
def go_forward(Advance_forward):
    '''
    リストを合計する

    parameters
    ----------
    Advance_forward : リスト[]
    リスト名を入れる

    Return
    ------
    sum関数で合計した値
    '''
    return sum(Advance_forward)

# 進みすぎた分戻る関数を定義
def go_back():
    '''
    goalを超えて戻る値

    Parameters
    ----------
    なし

    Return
    ------
    goalからリストに入ってる数を
    引いてそれを*2掛けした数
    '''
    return ((goal - sum(cur_x)) * 2)

while True:
    user = input('サイコロをふってください')
    if user == '':
        result = shake_dice()
        cur_x.append(result)
        if go_forward(cur_x) == goal:
            print('{}がでました。おめでとうございます、ゴールです！'.format(result))
            exit()
        elif go_forward(cur_x) > goal:
            cur_x.append(go_back())
            print('{}がでました。現在位置は{}です'.format(result, go_forward(cur_x)))
        else:
            print('{}がでました。現在位置は{}です。'.format(result, go_forward(cur_x)))
    else:
        print('サイコロを振るにはenterキーを押してください')
