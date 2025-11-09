
with open('E:\Exercise\Week2\ex3_data.txt', 'r' ) as f:
    document = f.read()

words = document.split()
dict2 = {}

for w in words:
    if w in dict2:
            dict2[w] += 1
    else:
            dict2[w] = 1
print(dict2)

