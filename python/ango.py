
def enc(k, m):
    code_a = 97  # 文字 a の文字コード
    kosu = 26    # 英字アルファベットの数
    leng = len(m)   # 文字列の長さ
    c = ""

    for i in range(leng):
        code = ord(m[i])  # i 文字目のコードを得る
        sa = code - code_a  # 文字 a からの差分
        if 0 <= sa and sa < kosu:
            sa = (k + sa) % 26  # 余りでアルファベット内を循環させる
        c = c + chr(sa + code_a)    # i番目の整数を文字に変換し文字列cの最後に連結

    return c

k=int(input())
hirabun = input()
angobun = enc(k, hirabun)
print(angobun)
