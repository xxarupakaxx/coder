import time

def existNumber(n, x):
    for i in range(len(x)):
        if x[i] == n:
            return i+1
    return -1
def a(i, j, x):
    while i < len(x):
        print(i + 1, ":", x[i])
        while j<len(x) and j>i:
            if x[i] == x[j]:
                return a(i + 1, j + 1, x)
                j = j + 1
        i=i+1
    return -1
print("分母 d を下さい")
d = int(input())
print("1 / ", d, " を求めます")

qList = [] #商の配列
rList = []  #余りの配列
stop = False
x = 1
leng = 0
a = 0
b = 0

while not stop:
    x = x * 10
    q = x//d
    r = x % d
    leng = leng + 1
    #print(leng, " : ", q)
    qList.append(q)
    rList.append(r)
    x = x % d
    
    
    if r == 0 and q !=0:
        stop = True
    #else:
       # y=existNumber(r,rList)
       # if y>=0:
       #  rList.append(r)
    if leng == d - 1:
        stop = True

a(0,0,qList)
            
    
        
    
    

             

         
        
                

         
         
         
         
        
