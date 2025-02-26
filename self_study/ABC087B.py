A = int(input())
B = int(input())
C = int(input())
X = int(input())

count = 0

for an in range(0, A+1):
  for bn in range(0, B+1):
    for cn in range(0, C+1):
      sum = 500 * an + 100 * bn + 50 * cn
      if sum == X:
        count = count + 1
        

print(count)
  
  