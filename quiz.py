
sum=0
new=0
suma=0
for i in range(1,1000):
    if i%3==0:
        sum+=i
    if i%5==0:
        new+=i
    if i%15==0:
        suma+=i
print(sum+new-suma)