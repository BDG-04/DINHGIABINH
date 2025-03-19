def dao_nguoc_list(lst):
    return lst[::-1]
#danh sach tu nguoi dung va xu lys chuoi
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
list_dao_nguoc = dao_nguoc_list(numbers)
print("List sau khi đảo ngược: ", list_dao_nguoc)