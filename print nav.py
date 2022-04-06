
'''i=1
while i<=100:
    if i%3==0:
        print("nav")
    if i%7==0:
        print("gurukul")
    elif i%3==0 or i%7==0:
        print("navgurukul") 
    else:
        print(i)      
    i=i+1'''

# i=55
# while i<=65:
#     a=i-55
#     print(a)
#     i=i+1

i=1
while i<=5:
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    print()
    i=i+1
