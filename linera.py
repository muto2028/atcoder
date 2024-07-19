import pulp
N = int(input())
Q = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))

INF = 10**18
ans = 0
for x in range(max(Q) + 1):
    y = INF
    for i in range(N):
        if Q[i] < A[i] * x:
            y = -INF
        elif B[i] > 0:
            y = min(y, (Q[i] - A[i] * x) // B[i])
    ans = max(ans, x + y)
print(ans)


import pulp
N = int(input())
Q = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))

a = [0] * N
b = [0] * N
problem = pulp.LpProblem('MAX', pulp.LpMaximize)
x = pulp.LpVariable('A',0,max(Q),'Integer')
y = pulp.LpVariable('B',0,max(Q),'Integer')

problem += x + y

for i in range(N):
    problem += x * A[i] + y * B[i] <= Q[i]

status = problem.solve()
c = int(x.value())
d = int(y.value())
print(c+d)

#結果表示
print("Result")
print("Curry:",x.value())
print("Oyako:",y.value())

















