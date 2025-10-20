def nhap_so_thu_tu(thu_tu):
    while True:
        value = input(f'nhap so nguyen duong {thu_tu}: ')
        if value.lstrip('-').isdigit(): # kiem tra co phai so nguyen khong
            number = int(value)
            if number > 0 :
                return number # tra ve khi hop le
            else:
                print("so khong thoa man, moi nhap lai: ")
        else:
            print("so khong thoa man, moi nhap lai: ")

tp = nhap_so_thu_tu(1)
fp = nhap_so_thu_tu(2)
fn = nhap_so_thu_tu(3)

precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1_score = 2 * ( precision * recall ) / (precision + recall) # tinh toan de bai

print(f'precision : {precision}')
print(f'recall : {recall}')
print(f'f1 score : {f1_score}')





