# tim max trong list va in ra
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]   #khai bao list
k = 3   #slicing window co kich thuoc bang 3
list1 =[]
kq = []

for element in num_list:
    #print(element)
    list1.append(element)
    #print(list1)
    if len(list1) == k:
        kq.append(max(list1))

        del list1[0]

print(kq)