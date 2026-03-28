#List Programs
#Create and display list
l=[20,70,40,60,10,39,10]
print(l)

#Sum and average of list
print("Sum= ", sum(l))
print("Average= ", (sum(l)/len(l)))

#max and min of list
print("Maximum number in the list= ", max(l))
print("Minimum number in the list= ", min(l))

#sorting of list
l.sort
print("Sorted list: ",l)

#Removing duplicates
l=list(set(l))
print(l)

#Merge two lists
l2=[50, 70]
print("Merged lists: ", l+l2)

#No. of odd end even
even=sum(1 for i in l if i%2==0)
odd=sum(1 for i in l if i%2!=0)
print("No. of even and odd elements: ", even, odd)

#To find second largest element in list
l.sort()
print("Secomd largest element= ",l[-2])

#List slicing
print(l[1:3])

#search a number
x=int(input("Enter the number to search in list l: "))
print("Found" if x in l else "Not found")
