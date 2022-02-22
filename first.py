from collections import defaultdict as dd
k=int(input())
ls=list(map(int,input().split()))[:k]
n=nd(int)
for i in ls:
   n[ls]=n[ls]+1
for i in n:
    print(i,"-",n[i])
