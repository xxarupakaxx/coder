# mult.py
# 入力: 自然数 x, y
# 出力: x × y

x = int(input())      # 入力された自然数を x に代入
y = int(input())      # 入力された自然数を y に代入
seki = 0              # 0 を seki に代入
while y > 0:          # y が 0 より大きい間は end までを繰り返す
    seki = seki + x   #   wa + 1 の値を wa に代入
    y = y - 1         #   y - 1 の値を y に代入
print(seki)            # seki の値を出力
