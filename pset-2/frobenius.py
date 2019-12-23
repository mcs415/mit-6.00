def find_representation(a, b, c, n):
  for i in range(n, -1, -a):
    for j in range(i, -1, -b):
      if not j % c:
        return True
  return False

def frobenius_number(a, b, c):
  a, b, c = sorted((a, b, c))
  base = n = c
  while True:
    if find_representation(a, b, c, n):
      if n == base + a:
        return base
    else:
      base = n
    n += 1

print(frobenius_number(6, 9, 20))
