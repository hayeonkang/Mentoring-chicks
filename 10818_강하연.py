#10818

N = int(input())
if not 1<=N<=1000000:
    False
A = list(map(int, input().split()))

min = A[0]
max = A[0]

for i in range(N):
    if not -1000000<=A[i]<=1000000:
        False
        
    if A[i] < min:
        min = A[i]
    if A[i] > max:
        max = A[i]
        
print(min, max)