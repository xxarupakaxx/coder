import time
# https://hack.jp/?p=254
# https://hack.jp/?p=252

def solve(n):
    turtle = 1
    rabit = 1
    start = 0
    end = 0

    if n > 0:
        while True:
            turtle = (turtle * 10) % n
            rabit=(rabit*10)%n
            rabit = (rabit * 10) % n
            if turtle == rabit :break
            
        if rabit != 0:
            rabit = 1
            start = 1
            while turtle != rabit:
                start = start + 1
                turtle = (turtle * 10) % n
                rabit = (rabit * 10) % n
            rabit = (rabit * 10) % n
            end =start
            while turtle != rabit:
                end = end + 1
                rabit = (rabit * 10) % n
    
    return start, end

print("分母 d を下さい")
d = int(input())
print("1 / ", d, " を求めます")

s, t = solve(d)
x = 1
print(s,t)
for i in range(0, t):
    x = x * 10
    q = x//d
    print(i + 1, ":", q)
    x = x % d
    
            


