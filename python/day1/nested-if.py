# nested-if.py
# 入力: 整数 a

a = int(input())      # 入力された整数を a に代入
if a < 0:
    print("N")        # Negative
else:
    if a == 0:
        print("Z")    # Zero
    else:
        print("P")    # Positive
        

