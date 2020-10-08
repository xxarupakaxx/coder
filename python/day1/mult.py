# mult.py
# 入力: 非負整数 x, y
# 出力: x * y

x = int(input())      # 入力された整数を x に代入
y = int(input())      # 入力された整数を y に代入
seki = 0              
while y > 0:          # y が 0 より大きい間は ブロックの実行を繰り返す
    seki = seki + x     
    y = y - 1           
print(seki)           
