def fukugou(k, angobun):
    code_a = 97  # 文字 a の文字コード
    kosu = 26  # 英字アルファベットの数
    leng = len(angobun)   # 文字列の長さ
    c = ""
    for i in range(leng):
        code=ord(angobun[i])
        sa = code - code_a
        if 0 <= sa and sa < kosu:
            sa = (-k + sa) % 26  # 余りでアルファベット内を循環させる
        c = c + chr(sa + code_a)  # i番目の整数を文字に変換し文字列cの最後に連結
    return c


k = int(input())
angobun = input()
fukubun = fukugou(k, angobun)
print(fukubun)
