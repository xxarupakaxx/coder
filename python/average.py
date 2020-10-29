def sum(a):     #関数の宣言
    n = len(a)  #配列の長さをnに代入
    sum = 0 #戻り値である配列aの要素の合計をおく
    for i in range(n):  #繰り返し実行
        sum = sum + a[i]    #   要素の合計の計算
    return sum  #戻り値としてsumをreturnする


a = list(map(int, input().split())) #　配列aの入力
print(sum(a)//len(a))   #配列aの要素の合計の平均値を出力
