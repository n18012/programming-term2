import random
unsei = [
    "大吉",
    "吉",
    "中吉",
    "小吉",
    "末吉",
    "凶",
    "大凶"]
a = random.randint(0, len(unsei)-1)

import random
naiyo = [
    "失せ物",
    "商売",
    "学問",
    "相場",
    "争事",
    "探し物",
    "恋愛"]
b = random.randint(0, len(naiyo)-1)

import random
advice = [
    "安し",
    "騒がず",
    "改めかえて",
    "障りあり",
    "平",
    "よろし",
    "出でず",
    "出ずべし",
    "誠意に答えよ"]
c = random.randint(0, len(advice) - 1)
result = "おみくじ： あなたの運勢は{0}です。{1}: {2}".format(unsei[a], naiyo[b], advice[c])
print(result)
