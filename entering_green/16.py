import itertools

N, K = map(int, input().split())
m = [list(map(int, input().split())) for l in range(N)]

l = []

for i in range(2, N+1):
  l.append(i)

alp = list(itertools.permutations(l, N-1))
count = 0

for j in range(len(alp)):
  sum = 0
  for k in range(0, N):
    # m[出発][到着]で値を取得する
    # 初回は必ず出発が都市1
    if k == 0:
      sum += m[0][alp[j][k]-1]
    # 最後は必ず到着が都市1
    elif k == N-1:
      sum += m[alp[j][k-1]-1][0]
    else:
      sum += m[alp[j][k-1]-1][alp[j][k]-1]

  if sum == K:
    count += 1


print(count)
