print('  |  1  2  3  4  5  6  7  8  9 ')
print('--+---------------------------')
for x in range(1, 10):
    print(' {}|'.format(x), end='')
    for y in range(1, 10):
        print('{:3}'.format(y * x), end='')
    print('')
