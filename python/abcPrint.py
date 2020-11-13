def dec(hirabun):
    leng = len(hirabun)   # 文字列の長さ
    c = ""
    t=0
    for i in range(leng):
       
        if leng <= 2 * i:
           break
        c += hirabun[2 * i]
    for i in range(leng):
        
        if leng <= 2 * i + 1:
            break
        c += hirabun[2 * i + 1]
    return c
hirabun = input()
t = dec(hirabun)
print(t)
