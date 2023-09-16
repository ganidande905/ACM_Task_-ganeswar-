t = int(input().strip())
if 1<=t<=10**5:
  for a0 in range(t):
    n = int(input().strip())
    if 1<=n<=10**9:
        a=1
        sum=0    
        while a<n:
            if a%3==0 or a%5==0:
                sum+=a
            a+=1
        print(sum)        