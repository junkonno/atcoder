N, A, B = map(int, input().split())
answer = []

for i in range(1, N+1):
  n = i
  l = [int(x) for x in list(str(n))]
  sum = 0
  
  for num in l:
    sum = sum + num
  
  if sum >= A and sum <= B:
    answer.append(i)

result = 0
for y in answer:
  result += y
  
print(result)