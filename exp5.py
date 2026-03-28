#Tuple
#creating tuple
t=(50,10,40,60,50)
print("Tuple: ", t)

#sum and average of tuple
sum=sum(t)
average=sum/len(t)
print("Sum= ", sum)
print("Average= ", average)


#maximum and minimun of tuple
print("Maximim= ", max(t))
print("Minimun= ", min(t))

#packing
t2=(1,2,3)

#unpacking
a, b, c = t2
print(a,b,c)

#converting tuple into list
l=list(t)
print("List: ", l)

#create and perform set operations
s={43,56,63,40,50}
s.add(25)
s.remove(40)
print("Set: ", s)

#Union, intersection and difference
s1={52,1,5,30,2,4,6}
s2={1,3,0,9}
print("Union: ", s1|s2)
print("Intersection: ", s1&s2)
print("Difference: ", s1-s2)

#Remove duplicate
unique=list(set(t))
print("Without duplication: ",unique)

#Check membership of element in tuple
x=20
if x in t:
    print("Element found")
else:
    print("Element not found")