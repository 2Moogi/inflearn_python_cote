n,k=map(int,input().split())
yaksu=[]
for i in range(1,n+1):
    if n % i ==0:
        yaksu.append(i)
if len(yaksu) < k:
    print(-1)
else:
    print(yaksu[k-1])

#약수

'''
n,k = map(int,input().split())
cnt=0
for i in range(1,n+1):
    if n%i == 0:
        cnt+=1
    if cnt == k:
        print(i)
        break
else:
    print(-1)
'''

#이렇게 생각할수도 있구나 하고 넘어가면 된다.
# 내 풀이가 나쁘다고 생각하지는 않음.
