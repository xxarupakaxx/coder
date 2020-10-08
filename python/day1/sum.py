# sum.py
# 入力: 非負整数 n
# 出力: 1 + 2 + ... + n

n = int(input())      # 入力された整数を n に代入
i = 1
sum = 0               # sum == 1 + .... + (i - 1)
while i <= n:
    sum = sum + i
    i = i + 1
print(sum)    
