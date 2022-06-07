a=int(input("enter any 3 digitn no"))
b=(a//100)**3
c=a%100
d=(c//10)**3
e=(c%10)**3

f=b+d+e

if f==a :
    print(a,"is a amstrong no.")
else :
    print(a,"is not a amstrong no.")