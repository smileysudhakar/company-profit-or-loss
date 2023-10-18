a=int(input("Company investment :"))
b=int(input("Manager :"))
c=int(input("Emp1 :"))
d=int(input("Emp2 :"))
e=int(input("Electrical charges :"))
f=int(input("Otherexpenses :"))
sum=b+c+d+e+f
Minimumamount=20000;
if (b <a and c <a and d <a and e <a and f <a):
    print("company is profit")
else:
    print("company is loss")