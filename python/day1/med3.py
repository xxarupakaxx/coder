# med3.py
# 入力: 整数 a, b, c
# 出力: a, b, c の中央値

a = int(input())      # 入力された整数を a に代入
b = int(input())      # 入力された整数を b に代入
c = int(input())      # 入力された整数を c に代入

if a < b:
    min = a           # 最小値の候補
    max = b           # 最大値の候補
else:
    min = b
    max = a
# この時点で，min <= max  

if ???:
    print(min)
elif ???:
    print(c)
else:
    print(max)
