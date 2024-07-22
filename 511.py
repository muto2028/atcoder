N = int(input())
A = list(map(int, input().split()))
sun = 0
for i in range(N-1):
    for k in range(i+1,N):
        sun += (A[i] + A[k]) % 100000000
print(sun)