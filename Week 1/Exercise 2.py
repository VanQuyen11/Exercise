import math

#hàm kiểm tra xem có là số hay không
def is_number(n):
    try:
        float(n)   # thử đưa chuỗi về kiểu `float`.
                   # nếu chuỗi không thuộc kiểu `float`,
                   # nó sẽ đưa ra `ValueError` exception
    except ValueError:
        return False
    return True

# hàm tương tác với người sử dụng
def exercise2():
    x = input('nhập x = ')
    if not is_number(x):
        print('x phải là số')
        return # exit()

    act_name = input('nhập  (sigmoid|relu|elu): ')
    x = float(x)
    result = calc_activation_func(x, act_name)
    if result is None:
        print(f'{act_name} không đúng')
    else:
        print(f'{act_name}: f({x}) = {result}')

# hàm tính toán và kiểm tra dữ liệu người dùng nhập vào
def calc_activation_func(x, act_name):
    def calc_relu(x):
        if x<=0:
            result = 0.0
        else:
            result = x
        return float(result)

    def calc_sig(x):
        return 1./(1+math.e**(-x))

    def calc_elu(x):
        alpha = 0.01
        result = None
        if x < 0:
            result = alpha*(math.e**x - 1)
        else:
            result = x
        return result

    result = None
    if act_name == 'relu':
        result = calc_relu(x)
    elif act_name == 'sigmoid':
        result = calc_sig(x)
    elif act_name == 'elu':
        result = calc_elu(x)
    return result

exercise2()

