def main():
    N = int(input())
    A = []
    for _ in range(N):
        A.append(input())
    M = int(input())
    B = []
    for _ in range(M):
        B.append(input())
    L = int(input())
    C = []
    for _ in range(L):
        C.append(input())
    Q = int(input())
    X = []
    for _ in range(Q):
        X.append(input())
    
    ans = []


    for i in range(Q):
        flag = 0
        if Q[i] < 3:
            ans[i] = 'No'
        num = Q[i]
        for k in range(N):
            num_A = num - A[k]
            if num_A < 3:
                continue
            for l in range(M):
                num_B = num_A - B[l]
                if num_B < 3:
                    continue
                for o in range(L):
                    num_C = num_B - C[o]
                    if num_C < 3:
                        continue
                    if num_C == 0:
                        ans[i] = 'Yes'
                        flag = 1
                        break
                if flag == 1:
                    break
            if flag == 1:
                break
        if flag == 1:
            break
        ans[i] = 'No'

        for s in range(Q):
            print(ans[s])
            

main()