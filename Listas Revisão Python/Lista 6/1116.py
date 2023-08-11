n = int(input())

for i in range(1, n+1):
  a,b = map(int,input().split())
  
  if b == 0:
    print('divisao impossivel')
  else:
    print(f'{a/b:.1f}')
