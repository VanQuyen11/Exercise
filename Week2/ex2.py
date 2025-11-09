word = 'baby helloworld'
dict1 = {}

for character in word:
    if character in dict1:
        dict1[character] += 1
    else:
        dict1[character] = 1

print(dict1)