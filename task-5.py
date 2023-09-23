res = []
for n in range(1, 1000):
  s = bin(n)[:2]
  
  if n % 2 == 0:
    binary = '1 + s + 0'
  else:
    binary = '11 + s + 00'
  if int(s, 2) < 52:
    
    res.append(int(s, 2))
print(min(res))
