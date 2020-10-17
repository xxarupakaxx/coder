# stringPrint.py
# 文字列処理の練習プログラム
# 入力: 文字列
# 出力: 文字列中の文字を一行ごとに出力する

print("文字列を入力しよう")
ss = input()          # 入力文字列を ss に格納
n = len(ss)           # 文字列の長さを変数 n に格納
for i in range(n):
    print(ss[i])
