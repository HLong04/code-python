def nhap_danh_sach_ke():
    danh_sach_ke = {}
    for i in range(1, 8):
        danh_sach_ke[i] = list(map(int, input(f"Nhập danh sách đỉnh kề của đỉnh {i} (cách nhau bằng dấu cách): ").split()))
    return danh_sach_ke

def in_dinh_ke(danh_sach_ke, dinh):
    if dinh not in danh_sach_ke:
        print(f"Đỉnh {dinh} không tồn tại.")
        return

    dinh_ke_list = danh_sach_ke[dinh]
    print(f"Các đỉnh kề của đỉnh {dinh}: {', '.join(map(str, dinh_ke_list))}")

# Nhập danh sách kề
print("Nhập danh sách kề:")
danh_sach_ke = nhap_danh_sach_ke()

# Nhập đỉnh i
i = int(input("Nhập đỉnh i (1 <= i <= 7): "))

# In ra đỉnh kề của đỉnh i
in_dinh_ke(danh_sach_ke, i)
