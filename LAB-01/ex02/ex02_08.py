#Hàm ktar số nhị phân có chia hết cho 5?
def chia_het_cho_5(so_nhi_phan):
    #chuyển số nhị sang thập
    so_thap_phan = int(so_nhi_phan, 2)
    #ktra số thập có chia hết cho 5?
    if so_thap_phan % 5 ==0:
        return True
    else:
        return False
    #Nhập chuối số nhị phân
chuoi_so_nhi_phan = input("Nhập chuỗi số nhị phân (Phân tách bởi dấu phẩy): ")
#tách chuối thành các số nhị phân và ktra chi hết cho5 ?
so_nhi_phan_list = chuoi_so_nhi_phan.split(',')
so_chia_het_cho_5 = [so for so in so_nhi_phan_list if chia_het_cho_5(so)]
#in ra các số nhị phân chia hết cho 5
if len(so_chia_het_cho_5) > 0:
    ket_qua = ','.join(so_chia_het_cho_5)
    print("Các số nhị phân chia hết cho 5 là: ", ket_qua)
else:
    print("Không có số nhị phần nào chia hết cho 5 trong chuỗi số vừa nhập.")
    