def sum(a):
    n = len(a)
    sum=0
    for i in range(n):
        sum = sum + a[i]
    return sum

a = list(map(int, input().split()))
print(sum(a)//len(a))
