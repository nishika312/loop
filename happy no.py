a=int(input("enter any number"))
num=a
while sum!=1 and sum!=4:
    sum=0
    while num!=0:
        rem=int(num%10)
        sum=sum+rem*rem
        num=num//10
    num=sum
    if sum==1:
        print(num,"is happy number")  
    else:
        print(num,"is not happy number")