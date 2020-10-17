print("文字列を入力しよう")
ss = input()          # 入力文字列を ss に格納
leng = len(ss)        # 文字列の長さを変数 leng に格納
for i in range(leng):   #繰り返して条件に合うものを探す
    if ord(ss[i]) >= 97 and  ord(ss[i]) <= 122:  # 小文字のASCIIコード
        print(ss[i])                            #出力する
