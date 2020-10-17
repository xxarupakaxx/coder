# junkan.py
# 配列の使い方の練習（循環小数を循環するまで求める）
# 入力: d
# 出力: 1/d の各桁を循環するまで求める

import time

print("分母 d を下さい")
d = int(input())
print("1 / ", d, " を求めます")

stop = False
leng = 0
x = 1
while not stop:
    x = x * 10
    q = x // d
    leng = leng + 1
    print(leng, ":", q)
    time.sleep(0.5)    
    x = x % d
    if x == 0: 
        stop = True
