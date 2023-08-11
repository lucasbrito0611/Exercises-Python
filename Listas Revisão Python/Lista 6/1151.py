n = int(input())

fib = [0,1]

for i in range(3, n+1):
  prox = fib[i-3] + fib[i-2]
  fib.append(prox)

if n == 1:
  print('0')
else:
  print(' '.join(map(str, fib)))
