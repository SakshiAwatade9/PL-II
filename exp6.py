#Dictionary
#create and display dictionary

student={"name":"Sakshi", "rollNo":24141001, "Marks":85}
print("Given dictionary: ", student)

#access keys, values and items
d={"a":1,"b":2, "c":3}
print("Keys: ", d.keys())
print("Values: ", d.values())
print("Items: ", d.items())

#Add and update elements
student["Year"]= "Second year IT"   #add
student["Marks"]= 90                #update
print(student)

#Delete elements
del d["b"]
print("Updated dictionary: ", d)

#merge two dictionaries
d2={"d":7, "e":9}
d.update(d2)
print("Merged dictionaries: ",d)

#students with highest marks
students={"A":90, "B":95, "C":91}
top=max(students, key=students.get)
print("Top student: ", top)

#sort dictionary by keys and values
d3={"b":2, "a":1, "c":3}
print("Sorted by keys: ", dict(sorted(d3.items())))                               #sorted by keys
print("Sorted by values: ", dict(sorted(d3.items(), key=lambda x: x[1])))         #sorted by values

#Dictionary compresion
d4={x:x*x*x for x in range(10)}
print("Compressed dictionary: ", d4)

#word frequency in sentence
s=input("Enter the sentence: ").split()
freq={}
for word in s:
    freq[word]= freq.get(word, 0) + 1
print(freq)