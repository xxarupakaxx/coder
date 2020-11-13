# hukugo.py
# 復号関数の定義と利用
# 入力: 文字列
# 出力: 復号した文字列

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
# 関数 dec （終）

##### プログラム本文 #####
# 暗号鍵の設定
k = 3

angobun = input()                    # 暗号文を入力
hirabun = dec(k, angobun)            # 平文に変換
print(hirabun)                       # 平文を出力
