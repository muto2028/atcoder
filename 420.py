N = int(input())
A = list(map(int, input().split()))
box = []

for i in range(N):
    flag = 0
    box.append(A[i])
    while True:
        l = len(box)
        if l == 1:
            break
        if box[l-1] != box[l-2]:
            break
        else: 
            key = box[l-1] + 1 
            box = box[:-2]
            box.append(key)

print(len(box))
            

            


while True:
    flag = 0
    for i in range(N-2):
        l = len(A)
        print(l-i-1,A)
        lf = l-i-2
        ri = l-i-1
        if A[lf] == A[ri]:
            key = A[lf] + 1
            del A[lf:ri+1]
            print("A:",A,lf,ri)
            A.insert(lf, key)
            i -= 1
            flag += 1

    if flag == 0:
        break

print(len(A))
