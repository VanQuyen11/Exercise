import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd

# Bài tập 1: Numpy Cơ Bản
# Câu nào sau đây là đúng để tạo mảng 1 chiều từ 0 đến 9

# arr = np.arange(0, 10,1)
# print(arr)

# #Cách tạo một mảng boolean 3x3 với tất cả giá trị là True

# arr = np . ones ((3 ,3) ) > 0
# print(arr)
# arr = np . ones ((3 ,3) , dtype = bool )
# print(arr)
# arr = np . full ((3 ,3) , fill_value = True , dtype = bool )
# print(arr)
#ca abc

# Câu hỏi 3: Kết quả của đoạn code sau đây:

# arr = np . arange (0 ,10)
# print ( arr [ arr %2 == 1])
# a ) [1 3 5 7 9]

# Câu hỏi 4: Kết quả của đoạn code sau đây:

# arr = np . arange (0 ,10)
# arr[ arr % 2 == 1] = -1
# print ( arr )
# b ) [ 0 -1 2 -1 4 -1 6 -1 8 -1]

# Câu hỏi 5: Kết quả của đoạn code sau đây:

# arr = np . arange (10)
# arr_2d = arr . reshape (2 , -1)
# print ( arr_2d )
# b ) [[0 1 2 3 4]
# [5 6 7 8 9]]

# Câu hỏi 6: Kết quả của đoạn code sau đây:

# arr1 = np . arange (10) . reshape (2 , -1)
# arr2 = np . repeat (1 ,10) . reshape (2 , -1)
# c = np . concatenate ([ arr1 , arr2 ] , axis =0)
# print (" Result : \n", c )
#
# Result :
#  [[0 1 2 3 4]
#  [5 6 7 8 9]
#  [1 1 1 1 1]
#  [1 1 1 1 1]]

# Câu hỏi 7: Kết quả của đoạn code sau đây:

# arr1 = np . arange (10) . reshape (2 , -1)
# arr2 = np . repeat (1 ,10) . reshape (2 , -1)
# c = np . concatenate ([ arr1 , arr2 ] , axis =1)
# print ("C = ", c )
#
# C =  [[0 1 2 3 4 1 1 1 1 1]
#  [5 6 7 8 9 1 1 1 1 1]]

# Câu hỏi 8: Kết quả của đoạn code sau đây:


# arr = np . array ([1 ,2 ,3])
# print ( np . repeat ( arr ,3) )
# print ( np . tile ( arr ,3) )
#
# [1 1 1 2 2 2 3 3 3]
# [1 2 3 1 2 3 1 2 3]

# Câu hỏi 9: Kết quả của đoạn code sau đây:

# a = np . array ([2 ,6 ,1 ,9 ,10 ,3 ,27])
# index = np . where ((a >=5) &( a <=10) )
# print (" result ", a [ index ])
#
# c ) [ 6 9 10]

# Câu hỏi 10: Kết quả của đoạn code sau đây:

# def maxx (x , y ) :
#    if x >= y :
#       return x
#    else :
#      return y
#
# a = np . array ([5 ,7 ,9 ,8 ,6 ,4 ,5])
# b = np . array ([6 ,3 ,4 ,8 ,9 ,7 ,1])
#
# pair_max = np . vectorize ( maxx , otypes =[ float ])
# print ( pair_max (a , b ) )
# # d ) [6. 7. 9. 8. 9. 7. 5.]

# Câu hỏi 11: Kết quả của đoạn code sau đây:

# a = np . array ([5 ,7 ,9 ,8 ,6 ,4 ,5])
# b = np . array ([6 ,3 ,4 ,8 ,9 ,7 ,1])
#
# print (" Result ", np . where (a <b , b , a ) )
# # a ) [6. 7. 9. 8. 9. 7. 5.]


# Bài tập 2: Xử lý ảnh

# Câu hỏi 12: Hoàn thành đoạn code sau đây để chuyển ảnh màu sang ảnh xám dựa vào
# phương pháp Lightness:


# img = mpimg . imread ('dog.jpeg' )
#
# def Colorgray(vector):
#     return np.max(vector) * 0.5 + np.min(vector) * 0.5
#
# Grayscale = np.apply_along_axis(Colorgray, axis=2, arr=img)
# plt.imshow(Grayscale, cmap = 'gray')
# plt.show()
# phương pháp Average:

# img = mpimg . imread ('dog.jpeg' )
#
# def Colorgray(vector):
#     return np.sum(vector)/3
#
# Grayscale = np.apply_along_axis(Colorgray, axis=2, arr=img)
# plt.imshow(Grayscale, cmap = 'gray')
# plt.show()

# phương pháp Luminosity:

# img = mpimg . imread ('dog.jpeg' )
#
# def Colorgray(vector):
#     return vector[0] * 0.21 + vector[1] * 0.72 + vector[2] * 0.07
#
# Grayscale = np.apply_along_axis(Colorgray, axis=2, arr=img)
# plt.imshow(Grayscale, cmap = 'gray')
# plt.show()

# Bài tập 3: Phân tích dữ liệu dạng bảng


# df = pd . read_csv ('advertising.csv')
#
# data = df . to_numpy ()

# Câu hỏi 15: Lấy giá trị lớn nhất và chỉ mục tương ứng của nó trên cột Sales:

# data = data[:5]
# sales_data = data[:, 3]
# sales_max = np.max(sales_data)

# hàm np.argmax để lấy giá trị index max

# sales_index = np.argmax(sales_data)
# print("MAX:", sales_max, '-' 'Index:', sales_index)

# Câu hỏi 16: Giá trị trung bình của cột TV là:
# tv_data = data[:, 0]
# # print(tv_data)
# tv_average = np.mean(tv_data)
# print(tv_average)

# Câu hỏi 17: Số lượng bản ghi có giá trị tại cột Sales lớn hơn hoặc bằng 20 là:

# sales_data = data[:, 3]
# # print(sales_data)
# sales_counter = np.sum(sales_data >= 20)
# print(sales_counter)

# Câu hỏi 18: Tính giá trị trung bình của cột Radio thoả mãn điều kiện giá trị tương ứng
# trên cột Sales lớn hơn hoặc bằng 15:

# sale_cond = data[:, 3] >= 15    #lấy giá trị cột sale rồi so sánh với 15 để ra ma trận boolen
# radio_data = data[:, 1]         #lấy giá trị cột radio

#radio_data nhân với sale_cond để loại những phần tử k đạt điều kiện ứng với cột sale_cond >= 15

# radio_cond = radio_data * sale_cond
# print(radio_cond)
# radio_mean = np.sum(radio_cond) / np.sum(sale_cond)
# print(radio_mean)

# Câu hỏi 19: Tính tổng các hàng của cột Sales với điều kiện giá trị Newspaper lớn hơn
# giá trị trung bình của cột Newspaper:

# sales_data = data[:, 3]       #lấy gia trị cột sale
# newspaper_data = data[:, 2]   #lấy giá trị cột newspaper
# newspaper_data_average = newspaper_data.mean()        # tính trung bình cột newspaper
# # print(newspaper_data_average)
#
# a = newspaper_data > newspaper_data_average       # so sánh điều kiện đề bài ---> tạo ma trận boolen
# sale_cond = sales_data * a                        # hủy các giá trị k đạt yêu cầu đề bài
# sale_sum = np.sum(sale_cond)
# print(sale_sum)

# Câu hỏi 20: Gọi giá trị trung bình của cột Sales là A. Tạo ra mảng mới scores chứa các
# giá trị Good, Average và Bad sao cho: nếu giá trị hiện tại > A => giá trị trong mảng mới
# là Good, < A thì sẽ là Bad và = A sẽ là Average. Sau đó in ra kết quả scores[7:10]

# sales_data = data[:, 3]                  #lấy gia trị cột sale
# sales_data_average = sales_data.mean()   # tính trung bình
#
# # tạo ma trận
# score_data = np.where(sales_data < sales_data_average, 'BAD',
#              np.where(sales_data >= sales_data_average, 'GOOD','AVERAGE')
#                       )
# print(score_data[7:10])

# Câu hỏi 21: Gọi giá trị trên cột Sales gần nhất với giá trị trung bình cũng chính cột
# Sales là A. Tạo ra mảng mới scores chứa các giá trị Good, Average và Bad sao cho: nếu
# giá trị hiện tại > A => giá trị trong mảng mới là Good, < A thì sẽ là Bad và = A sẽ là
# Average. Sau đó in ra kết quả scores[7:10]

# sales_data = data[:, 3]
# sales_mean = sales_data.mean()
# average_index = np.argmin(abs(sales_data - sales_mean))       #lấy index mà có giá trị gần min
# b = sales_data[average_index]                                 #lấy giá trị từ index
# # print(b)
#
# # tạo ma trận
# score_data = np.where(sales_data < sales_mean, 'BAD',
#            np.where(sales_data >= sales_mean, 'GOOD','AVERAGE')
#                        )
# print(score_data[7:10])




