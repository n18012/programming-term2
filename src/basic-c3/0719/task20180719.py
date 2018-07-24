# 四則演算プログラム
arithmetic = {
        '+': 0,
        '-': 1,
        '*': 2,
        '/': 3,
}
# 出力
print("四則演算プログラムです。")
while True:
    try:
        user1 = float(input('第１パラメーターを入力してくだい>>>'))
    except ValueError:   # 数値が入らなければエラー表示されループが回る
        print('エラーです。再度入力してください')
        continue
    else:
        break

while True:
    try:
        user2 = float(input('第２パラメーターを入力してくだい>>>'))
    except ValueError:
        print('エラーです。再度入力してください')
        continue
    else:
        break

while True:
    arithmetic_word = input('計算方法を入力してください>>>')
    if arithmetic_word in arithmetic.keys():
        break
    else:
        print('エラーです。再度入力してください')

# 計算する関数
    def add(para1, para2):
        '''
        Parameters
        ----------
        para1 : int or float
        para2 : int or floar
        Returns
        -------
        para1とpara2を足した値
        '''
        return para1 + para2

    def mul(para1, para2):
        '''
        掛け算を行う
        Parameters
        ----------
        para1: float or int
        para2: float or int
        Returns
        -------
        para1とpara2をかけた値
        '''
        return para1 * para2

    def sub(para1, para2):
        '''
        引き算を行う
        Parameters
        ----------
        para1: float or int
        para2: float or int
        Returns
        -------
        para1とpara2を引いた値
        '''
        return para1 - para2

    def div(para1, para2):
        '''
        割り算を行う
        Parameters
        ----------
        para1: float or int
        para2: float or int
        Returns
        -------
        para1とpara2を割った値
        '''
        return para1 / para2

# 入力された値を作った関数で計算
if arithmetic_word == '+':
    result = add(user1, user2)
elif arithmetic_word == '-':
    result = sub(user1, user2)
elif arithmetic_word == '*':
    result = mul(user1, user2)
elif arithmetic_word == '/':
    result = div(user1, user2)

# 小数点第３位まで丸める
result = round(result, 3)
print('結果は{}です'.format(result))
