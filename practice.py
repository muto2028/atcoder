N, M = map(int, input().split())
A = list(map(int, input().split()))

m = 0
for i in range(1,N+1):
    if i == A[m]:
        print('0')
        m += 1
        continue
    if i > A[m]:
        m += 1
        i -=1
        continue
    print(A[m] - i)


    


                

