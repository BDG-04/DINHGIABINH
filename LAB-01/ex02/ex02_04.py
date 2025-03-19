#tạo một danh sách rỗng đễ lưu kết quả
j = []
# Duyệt qua tất cả các số từ 2000-3200, ktra số i có chia hết 7 và ko phải bội của 5
for i in range(2000, 3201):
    if (i % 7 == 0 ) and (i %5 != 0):
        j.append(str(i))
print(',' .join(j))
