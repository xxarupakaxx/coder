# smile2.py
# 出力: スマイルマークが，どうなるか？

import time

d1 =  1000000000000000000000000000
d2 =  1000000000110000110000000000
d3 =  1000000000110000110000000000
d4 =  1000000000000000000000000000
d5 =  1000001100000000000011000000
d6 =  1000000110000000000110000000
d7 =  1000000011000000001100000000
d8 =  1000000000111111110000000000
d9 =  1000000000000000000000000000
d10 = 1000000000000000000000000000

t = 0

while t < 29:
    print(d1)
    print(d2)
    print(d3)
    print(d4)
    print(d5)
    print(d6)
    print(d7)
    print(d8)
    print(d9)
    print(d10)
    print()                      # 空行を出力

    time.sleep(0.1)                  # 0.1秒休む

    d1 = d1 // 10
    d2 = d2 // 10
    d3 = d3 // 10
    d4 = d4 // 10
    d5 = d5 // 10
    d6 = d6 // 10
    d7 = d7 // 10
    d8 = d8 // 10
    d9 = d9 // 10
    d10 = d10 // 10

    t = t + 1

