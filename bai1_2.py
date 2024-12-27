def kiem_tra_chuoi_nhi_phan(chuoi):
    return all(ky_tu in ['0', '1'] for ky_tu in chuoi)

def chuyen_nhi_phan_sang_thap_phan(chuoi):
    if not kiem_tra_chuoi_nhi_phan(chuoi):
        return "Chuỗi không phải là chuỗi nhị phân."

    so_thap_phan = int(chuoi, 2)
    return so_thap_phan

# Thử nghiệm
chuoi_nhi_phan = input("Nhập chuỗi nhị phân: ")

try:
    so_thap_phan = chuyen_nhi_phan_sang_thap_phan(chuoi_nhi_phan)
    print(f"Số ở hệ thập phân: {so_thap_phan}")
except ValueError:
    print("Chuỗi không phải là chuỗi nhị phân.")
