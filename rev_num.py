#reverse a number
num=int(input('enter a number:'))
last_dig=0
rev=0
while(num>0):
    last_dig=num%10
    rev=rev*10+last_dig
    num=num//10
print('the reversed number is=',rev)

