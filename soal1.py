N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

lawan = sorted(zip(a, b))

for a, b in lawan:
  if a <= M:
    M+=b
  else:
    break
print(M)
