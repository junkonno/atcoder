X, K, D = map(int, input().split())

ans = 0

#1-3はMECE
#1.Xの絶対値よりもK*Dが小さい場合
#abs(X)に向かって一番近づく。
if abs(X) > K*D:
  ans = abs(X) - (K*D)

#2.Xの絶対値とK*Dが同じ場合
#abs(X)に向かって一番近づいて0になる。
elif abs(X) == K*D:
  ans = 0

#3.Xの絶対値よりもK*Dが大きい場合
elif abs(X) < K*D:
  #XがDで割り切れてしまう場合
  if abs(X) % D == 0:
    if (K - (abs(X)/D)) % 2 == 0:
      ans = 0
    elif (K - (abs(X)/D)) % 2 == 1:
      ans = abs(D)
  #XがDで割り切れない場合
  else:
    #K-商が偶数なら
    if (K - (abs(X)//D)) % 2 == 0:
      ans = abs(X) % D
    #K-商が奇数なら
    elif (K - (abs(X)//D)) % 2 == 1:
      ans = abs((abs(X) % D) - D)

print(ans)
