'''
#4번_2739
N = int(input())

for i in range(9):
    print(N, "*" , (i+1), "=", N*(i+1))


#5번_8393
sum = 0
N = int(input())
for i in range(N):
    sum += (i+1)
print(sum)
'''

#6번_10871
a,b = input().split()
a=int(a)
b=int(b)
for i in range(a):
    c = int(input())
    if c<b:
        print(c)
        
'''

#7번_10951
while (True):
    A, B = input().split()
    if A!=EOF & B!=EOF:
        A = int(A)
        B = int(B)
        print(A+B)
    else:
        break

'''