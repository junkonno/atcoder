N = int(input())

A = [] 
for _ in range(N):
  A.append(int(input()))
  
list = sorted(A, reverse=True)

ans = []
ans.append(list[0])

for x in range(1, N):
  if list[x] < list[x-1]:
    ans.append(list[x])

print(len(ans))
