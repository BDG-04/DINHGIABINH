def truy_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element

#Nhap tu nguoi dung
input_tuple = eval(input(" Nhập tuple, vd: (1,2,3 ): "))
first, last = truy_cap_phan_tu(input_tuple)

print("Phần tử đầu tiên: ", first)
print("Phần từ cuối cùng: ", last)