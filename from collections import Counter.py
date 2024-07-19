from collections import Counter

def chek(num):
    digits = str(num)
    for i in range(len(digits) - 1):
        if digits[i] == digits[i + 1]:
            return True
    return False

T = int(input())
K = []
for _ in range(T):
    K.append(int(input()))

for i in range(T):
    flag = 0
    k = 0
    while True:
        flag += 1
        k += 1
        if chek(k):
            flag -= 1
        if K[i] == flag:
            print(k)
            break



