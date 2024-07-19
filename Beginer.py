def check(N, A, B, D, num):
    week = A + B
    for i in range(N):
        smp = D[i] + num
        if smp > week:
            smp = smp - week     
        if A+1 <= smp <= week:
            return False
    return True


N, A, B = map(int, input().split())
D = list(map(int, input().split()))
week = A + B
flag = False
for i in range(week+1):
    if check(N, A, B, D, i):
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")




     
