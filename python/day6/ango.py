# ango.py
# 暗号化関数の定義と利用
# 入力: 文字列
# 出力: 暗号化した文字列

# 平文を暗号化する関数
# enc(秘密鍵 k, 平文 m) = 暗号文 c
def enc(k, m):
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
        c = c + chr(sa + code_a)    # 暗号文用のコードの格納
    return c
# 関数 enc （終）

##### プログラム本文 #####
# 暗号鍵の設定
k = 3

hirabun = input()                    # 平文を入力
angobun = enc(k, hirabun)            # 暗号文に変換
print(angobun)                       # 暗号文を出力
