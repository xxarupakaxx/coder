# mult2.py
# 入力: 自然数 x, y
# 出力: x × y

x = int(input())            # 入力された自然数を x に代入
y = int(input())            # 入力された自然数を y に代入
seki = 0                    # 0 を seki に代入
while y > 0:                # y が 0 より大きい間は ブロック までを繰り返す
    a = seki                # 和のプログラム add.py を挿入
    b = x
    wa = a   
    while b > 0:
        wa = wa + 1
        b = b - 1
    seki = wa               #   wa の値 (seki + x) を seki に代入
    y = y - 1               #   y - 1 の値を y に代入
print(seki)                 # seki の値を出力
