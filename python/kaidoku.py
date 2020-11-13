def kaidokou(anogoubun):

    code_a = 97  # 文字 a の文字コード
    kosu = 26  # 英字アルファベットの数
    hindo = [0] * kosu
    leng = len(angoubun)  # 文字列の長さ
    #code_e = code_a + 4
    for i in range(leng):
        code = ord(angoubun[i])
        sa = code - code_a
        if sa>=0 and sa<=25:
         hindo[sa] = hindo[sa] + 1
    max = -1
    maxj = -1
    for i in range(len(hindo)):
        if max < hindo[i]:
            max = hindo[i]
            maxj = i
    if maxj>=4:
        k = maxj - 4
    else:
        k = 4 - maxj

    return k

angoubun = input()
k = kaidokou(angoubun)
print(k)
     
        


