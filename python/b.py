def hukugo(ango):
    leng = len(ango)
    c = ""
    oddN=leng//2
    evenN = leng // 2 + 1
    if leng%2==1:
        for i in range(0,evenN):
            if evenN + i >= leng:
                c += ango[i]
                break
            c += ango[i]
            c += ango[evenN + i]
        return c
    else:
        for i in range(0, oddN):
            if oddN + i >= leng:
                c += ango[i]
                break
            c += ango[i]
            c += ango[oddN + i]
        return c


hirabun = input()
t = hukugo(hirabun)
print(t)
    
        
