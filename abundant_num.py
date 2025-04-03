num=int(input('enter a number'))
s=num
summ=0
for i in range(1,num//2+1):
    if(num%i==0):
        summ=summ+i
        i+=1
print("sum of all the divisor is:")
print(summ)
if(summ>s):
    print('it is an abundant number')
else:
    print('it is not an abundant number')
