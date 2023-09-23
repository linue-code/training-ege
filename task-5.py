for n in range(1,1000):
  s = bin(n)[:2]
  if s % 2 == 0:
    processed_binary = '1 + s + 0'
  else:
    processed_binary = '11 + s + 00'
  return int(processed_binary,2)
  
