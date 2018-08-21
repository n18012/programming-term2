res = [
    "アホ" if i % 3 == 0 else str(i)
    if 30 >= i else "アホ"
    if 39 >= i else str(i)
    for i in range(1, 41)]
print(res)
