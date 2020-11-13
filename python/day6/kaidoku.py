# kaidoku.py
# 解読プログラム
# 入力: 暗号文の文字列
# 出力: 復号した平文

# 暗号文を復号する関数
# dec(秘密鍵 k, 暗号文 m) = 平文 c
def dec(k, m):
    code_a = 97                    # 文字 a の文字コード
    kosu = 26                      # 英字アルファベットの数
    leng = len(m)                  # 文字列の長さ
    c = ""

    for i in range(leng):
        code = ord(m[i])            # i 文字目のコードを得る
        sa = code - code_a          # 文字 a からの差分
        #
        # ここに埋め込む
        #
        c = c + chr(sa + code_a)    # 平文用のコードの格納
    return c
# サブルーチン dec （終）

##### プログラム本文 #####
# 入力と準備
code_a = 97                  # 文字 a の文字コード
kosu = 26                    # 英字アルファベットの数
angobun = input()            # 暗号文を入力（注：入力文字列から改行を除去）
leng = len(angobun)          # 暗号文の長さを leng に格納
hindo = [0] * kosu           # 頻度配列の準備

# 頻度配列の作成
for i in range(leng):
    code = ord(angobun[i])   # i 文字目のコードを得る
    sa = code - code_a       # 文字 a からの差分
    #
    # ここに埋め込む
    #
    
print(hindo)  ## 確認用

# 最頻文字の位置（差分）の確定
max = 0
maxj = -1
for j in range(kosu):
    if hindo[j] > max:
        max = ...                 # ここも埋める
        maxj = ...                # ここも埋める
    
print(max, maxj)  ## 確認用

k = maxj - 4                # maxj - 4 が負の場合もＯＫのはず（dec の作り方に依存）
hirabun = dec(k, angobun)   # この暗号鍵で平文に変換
print(hirabun)              # 解読平文を出力
