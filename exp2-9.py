n=int(input("Enter any number: "))
count=0
while n!=0:
    n//=10
    count+=1
    print("No. of digits:", count)