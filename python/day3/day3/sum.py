# sum.py
# 入力: 空白で区切られた整数の列
# 出力: 入力された整数の総和

a = list(map(int, input().split()))
n = len(a)
# 以下が総和の計算部分
s = 0
for k in range(n):
    s = s + a[k]
print(s)

