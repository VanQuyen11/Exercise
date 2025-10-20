import math
import random

# hàm tính mae
def calc_mae(n):
    mae = 0
    for i in range(n):
        y = random.random()
        yhat = random.random()
        print(f"y = {y} | yhat = {yhat}")
        abs_error = abs(y - yhat)
        mae = mae + abs_error
    mae = mae / n
    return mae

#hàm tính mse
def calc_mse(n):
    mse = 0
    for i in range(n):
        y = random.random()
        yhat = random.random()
        print(f"y = {y} | yhat = {yhat}")
        error = (y - yhat)**2
        mse = mse + error
    mse = mse / n
    return mse

#hàm tính rmse
def calc_rmse(n):
    mse = 0
    for i in range(n):
        y = random.random()
        yhat = random.random()
        print(f"y = {y} | yhat = {yhat}")
        error = (y - yhat)**2
        mse = mse + error
    mse = mse / n
    rmse = math.sqrt(mse)
    return rmse

print(calc_mae(10))
print(calc_mse(10))
print(calc_rmse(10))



