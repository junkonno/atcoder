N = int(input())
A = list(map(int, input().split()))

list = sorted(A, reverse=True)

alice_list = []
bob_list = []

for x in range(N):
  if x == 0 or x % 2 == 0:
    alice_list.append(list[x])
    
  else:
    bob_list.append(list[x])

sum_alice = 0
sum_bob = 0

for num1 in alice_list:
  sum_alice += num1
  
for num2 in bob_list:
  sum_bob += num2

result = sum_alice - sum_bob

print(result)
