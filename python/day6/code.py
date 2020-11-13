# code.py
# 文字列処理の復習用
# 入力: 文字列
# 出力: 文字列の文字で小文字のみ，文字と各種情報を出力する

# 初期設定
code_a = 97                 # 文字 a の文字コード
kosu = 26                   # 英字アルファベットの数

# 入力
bun = input()               # 入力文字列
leng = len(bun)

print("** 文字，文字コード，a からの差分**")
for i in range(leng):
    moji = bun[i]            # bun の i 文字目を得る (i は 0から始まる)
    code = ord(moji)           # その文字のコードを得る
    sabun = code - code_a
    if 0 <= sabun and sabun < kosu:               # 小文字アルファベットならば
        print(moji, ": ", code, ", ", sabun)      # 　情報を表示する
    else:                                         # そうでないときは
        print(moji, ": ", code)                   # 　差分は表示しない


