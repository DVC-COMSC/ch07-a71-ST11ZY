
numbers = list(map(int, input().split()))
total=sum(numbers)
avg=total/10
x=len(numbers)
for i in range (x):
    dist=numbers[i]-avg
    if dist>0:
        print (f'{dist:.2f}', end=' ')
    if dist<0:
        dist=avg-numbers[i]
        print(f'{dist:.2f}',end=' ')
