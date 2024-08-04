#Nを受け取る
N = int(input())
#リストを受け取る
A = list(map(int, input().split()))

#大カウントを定義する
big_count = 0
little_count = N

#小カウントがNの間実行する
while little_count == N:

  #小カウントをリセットする
  little_count = 0
  #1個ずつリストの数字に対して処理する
  for x in A:
    #もし余りが0なら
    if x % 2 == 0:
      #リストの小カウント番目の数字を割る2した値に置き換え
      A[little_count] = x//2
      #小カウント+1
      little_count += 1
      
      #大カウントを+1する
      if little_count == N:
        big_count += 1
      
    #もし余りが1以上なら
    if x % 2 > 0:
      #処理を終了する
      break
    
 

#大カウント数を出力する
print(big_count)