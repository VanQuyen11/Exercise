# tim max trong list va in ra
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]   #khai bao list
k = 3
list1 = []
kq = []
start_index = list(range(0, len(num_list) - k + 1))
end_index = list(range(k, len(num_list) + 1))

for start_index, end_index in zip(start_index, end_index):
    list1 = num_list[start_index:end_index]
    kq.append(max(list1))

print(kq)


