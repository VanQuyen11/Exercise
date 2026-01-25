import numpy as np
import cv2


# tinh độ dài vector

# def compute_vector_length ( vector ) :
#     len_of_vector = np.linalg.norm( vector )       # hàm np.linalg.norm để tính độ dài vector
#     return len_of_vector
#
# #test     KQ = 3.741
# data = np.array([1,2,3])
# print(compute_vector_length(data))

# tính tích vô hướng

# def compute_dot_product ( vector1 , vector2 ) :
#     result = vector1.dot(vector2)                  #hàm dot để tính tich vô hướng
#     return result

#test   KQ = 32
# data1 = np.array([1,2,3])
# data2 = np.array([4,5,6])
# result = compute_dot_product(data1, data2)
# print(result)

# nhân vector với ma trận

# def matrix_multi_vector(matrix, vector):
#     result = vector.dot(matrix)
#     return result
#
# #test   KQ = [ 50 122]
# data1 = np.array([[1, 2, 3], [4, 5, 6]])
# data2 = np.array([7,8,9])
# result = matrix_multi_vector(data2, data1)
# print(result)

# nhân vector với vector

# def matrix_multi_matrix(matrix1, matrix2):
#     result = np.dot(matrix1, matrix2)
#     return result

#test    KQ =[[ 30  36  42]
            #[ 84  99 114]]
# data1 = np.array([[1, 2, 3], [4, 5, 6]])
# data2 = np.array([[7, 8, 9], [10, 11, 12],[1,2,3]])
# result = matrix_multi_matrix(data1, data2)
# print(result)

# tính ma trận nghịch đảo

# def inverse_matrix(matrix):
#     det_matrix = np.linalg.det(matrix)                      #hàm det để tính định thức
#     if det_matrix == 0:
#         raise ValueError("Matrix is singular and not invertible")
#     return np.linalg.inv(matrix)                            # hàm inv để tính ma trận nghịch đảo
#
# # test      KQ = [[-1.66666667  0.66666667]
#                  [ 1.33333333 -0.33333333]]
# data1 = np.array([[1, 2], [4, 5]])
# inv_data1 = inverse_matrix(data1)
# print(inv_data1)

# tính Eigenvector và eigenvalues:

# def compute_eigenvalue_eigenvector(matrix):
#     eigenvalue, eigenvector = np.linalg.eig(matrix)
#     return eigenvalue, eigenvector
#
# #test      KQ =    [-1.  7.]
#                    [[-0.83205029 -0.4472136 ]
#                    [ 0.5547002  -0.89442719]]
# matrix = np.array([[1,  3], [4, 5]])
# eigenvalue, eigenvector = compute_eigenvalue_eigenvector(matrix)
# print(eigenvalue)
# print(eigenvector)

# tính cosine_similarity

# def compute_cosine(v1, v2):
#     cos_sim = np.dot(v1,v2) / ((np.linalg.norm(v1) * np.linalg.norm(v2)))
#     return cos_sim
#
# #test      KQ  =  0.5773502691896257
# x = np.array([1, 2, 3, 4])
# y = np.array([1, 0, 3, 0])
# print(compute_cosine(x, y))

# Background subtraction

IMG_SIZE = (678, 318)

# đọc ảnh từ local
bg1_image = cv2.imread('GreenBackground.png', 1)       #1 là ảnh màu,  0 là ảnh xám
bg1_image = cv2.resize(bg1_image, IMG_SIZE)     # resize image

ob_image = cv2.imread('Object.png', 1)
ob_image = cv2.resize(ob_image, IMG_SIZE)

bg2_image = cv2.imread('NewBackground.jpg', 1)
bg2_image = cv2.resize(bg2_image, IMG_SIZE)

def compute_differences(bg_image, input_image):
     difference = cv2.absdiff(bg_image, input_image)
     difference_single = np.sum(difference, axis=2) / 3.0
     return difference_single

def compute_binary_mask ( difference_single ) :
    difference_binary = np.where(difference_single >= 15, 255, 0)
    difference_binary = np.stack((difference_binary,) * 3, axis=-1)
    difference_binary = difference_binary.astype(np.uint8)
    return difference_binary

def replace_background ( bg1_image , bg2_image , ob_image ) :
    difference_single = compute_differences(bg1_image, ob_image)
    binary_mask = compute_binary_mask ( difference_single )
    output = np.where(binary_mask == 255, ob_image, bg2_image)
    return output

output = replace_background(bg1_image, bg2_image, ob_image)
cv2.imshow('output', output)
cv2.waitKey(0)
cv2.destroyAllWindows()