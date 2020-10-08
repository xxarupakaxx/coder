# max3.py
# 入力: 整数 a, b, c
# 出力: a, b, c の最大値

a = int(input())      # 入力された整数を a に代入
b = int(input())      # 入力された整数を b に代入
c = int(input())      # 入力された整数を c に代入
max = a               # a の値を最大値の候補とする
if b > max:
    max = b
if c > max:
    max = c
print(max)             # max の値を出力

