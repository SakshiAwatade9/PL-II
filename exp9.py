#Create and write data into file
file = open("sample.txt", "w")
file.write("Hello, this is first file.\nWelcome to file handling.")
file.close()
print("Data written successfully.")

#Read data from file
file = open("sample.txt", "r")
data = file.read()
print(data)
file.close()

#Append data into the file
file = open("sample.txt", "a")
file.write("\nThis is appended text.")
file.close()
print("Data appended successfully.")

#Counts lines, words, and characters 
file = open("sample.txt", "r")
data = file.read()

lines = data.split("\n")
words = data.split()
characters = len(data)

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", characters)

file.close()

#Copy contents from one file to another
source = open("sample.txt", "r")
content = source.read()

destination = open("copy.txt", "w")
destination.write(content)

source.close()
destination.close()

print("File copied successfully.")

#Handle division by zero exception
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
    
#Handle Invalid Input Exception
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Error: Invalid input. Please enter a number.")
    
#Use try–except–finally Block
try:
    file = open("sample.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution completed.")
    
    
#User-Defined Exception
class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    print("You entered:", num)
except NegativeNumberError as e:
    print("Error:", e)
    
#File Exception Handling
try:
    file = open("unknown.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Error: File does not exist.")
except IOError:
    print("Error: Unable to read file.")