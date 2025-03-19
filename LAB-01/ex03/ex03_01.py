def sum_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 ==0:
            tong += num
    return tong
 # Nhap danh sach tu ng dung va xu ly
input_list = input("nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
tong_chan = sum_so_chan(numbers)
print("Tổng số chẵn trong Lít là: ", tong_chan)
