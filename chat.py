def find_neq_number(K):
    count = 0
    num = 0
    
    while True:
        num += 1
        if '11' in str(num):
            continue
        count += 1
        if count == K:
            return num

# テストケースの数
T = int(input())
K = [int(input()) for _ in range(T)]

for i in range(T):
    print(find_neq_number(K[i]))

