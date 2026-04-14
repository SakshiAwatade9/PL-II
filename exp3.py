#Length of string
string = input("Enter a string: ")
print("Length of string:", len(string))

#Reverse of string
string = input("Enter a string: ")
reversed_string = string[::-1]
print("Reversed string:", reversed_string)

#Check Palidrome
string = input("Enter a string: ")

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
    
#Count vowels and consonents
string = input("Enter a string: ").lower()

vowels = "aeiou"
v_count = 0
c_count = 0

for ch in string:
    if ch.isalpha():
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)

#Converting upper and lower case
string = input("Enter a string: ")

print("Uppercase:", string.upper())
print("Lowercase:", string.lower())

#Frequency of characters
string = input("Enter a string: ")
freq = {}

for ch in string:
    freq[ch] = freq.get(ch, 0) + 1

print("Character frequency:")
for key, value in freq.items():
    print(key, ":", value)
    
#Remove space from string
string = input("Enter a string: ")

result = string.replace(" ", "")
print("Without spaces:", result)

#Splits and join strings
string = input("Enter a string: ")

words = string.split()   # split into list
print("Split:", words)

joined = "-".join(words)
print("Joined:", joined)

#Check Anagrams
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1) == sorted(str2):
    print("Anagrams")
else:
    print("Not Anagrams")