#入力
N = int(input())
t = [0] * N
x = [0] * N
y = [0] * N
for i in range(N):
    t[i], x[i], y[i] = map(int, input().split())
    
now_place = [0, 0]
now_time = 0
count = 0

for a in range(N):
  next_place = [x[a], y[a]]
  distance = abs((next_place[0] + next_place[1])-(now_place[0] + now_place[1]))
  time = t[a] - now_time
  
  if time >= distance:
    if distance % 2 == 0:
      if time % 2 == 0:
        count+=1
        now_place = [x[a], y[a]]
        now_time = t[a]
      else:
        break
    if distance % 2 != 0:
      if time % 2 != 0:
        count+=1
        now_place = [x[a], y[a]]
        now_time = t[a]
        
  else:
    break

if count == N:
  print("Yes")
else:
  print("No")