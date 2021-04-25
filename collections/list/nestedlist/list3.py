vowels=["a","e","i","o","u"]
words=input("Enter some words to search vowels: ")
found=[]
for letter in words:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
print(found)