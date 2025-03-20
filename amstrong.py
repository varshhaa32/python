#amstrong number
num=int(input('enter the number:'))
count=0
temp=num
c=num
while(num>0):
    num=num//10
    count+=1
print('the number of digits=',count)
last_dig=0
summ=0
while(temp>0):
    last_dig=temp%10
    p=last_dig**count
    summ=summ+p
    temp=temp//10
print('The sum is=',summ)
if(summ==c):
    print('it is an amstrong number')
else:
    print('it is not an amstrong number')
