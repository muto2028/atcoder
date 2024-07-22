N = int(input())
A = list(map(int, input().split()))
lim = 100000000
A = sorted(A)

sun = 0
for i in range(N):
    if A[i] + A [N-1] < 100000000:
        sun += A[i] * N -1
        sun += sum(A[i+1:])
    else:
        for k in range(i + 1, N):
            if A[i] + A [N- 1 - k] < 100000000:
                print(sun)