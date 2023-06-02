N=int(input())
coefficients=list(map(int,input().split()))
x=int(input())
sum=0
for i in range(N+1):
    sum=coefficients[i]*pow(x,i)+sum
print(sum)
    
                        
    
    