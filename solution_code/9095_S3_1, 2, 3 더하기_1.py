# 9095 -> 정답

num = int(input())
q = []
for i in range(num):
  q.append(int(input()))

# 2,3

def ans(n):
  d = [0, 1, 2, 4] + [0] * (n-3)

  for i in range(4, n+1):
    d[i] = d[i-1] + d[i-2] + d[i-3]

  print(d[n])

for n in q:
  ans(n)