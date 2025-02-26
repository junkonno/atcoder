N, Y = map(int, input().split())

list = []
count=0

for x in range(0, N+1):
  for y in range(0, N-x+1):
      z = N - x - y
      sum = 10000 * x + 5000 * y + 1000 * z
        
      if sum == Y:
        ans = []
        ans.append(x)
        ans.append(y)
        ans.append(z)
        list.append(ans)
        count +=1
        
if count == 0:
  print("-1 -1 -1")
else:
  print(str(list[0][0]) + " " + str(list[0][1]) + " " + str(list[0][2]))
