def nhap():
    mahp = input("Nhập mã học phần: ")
    tenhp = input("Nhập tên học phần: ")
    sotc = input("Nhập số tín chỉ: ")

    return {"mahp": mahp, "tenhp": tenhp, "sotc": sotc}

def xuat(danhsach):
    print("Các học phần thuộc CNTT: ")
    for hoc_phan in danhsach:
        if hoc_phan["mahp"][:3] == "TIN":
            print(f"Mã học phần: {hoc_phan['mahp']}, Tên học phần: {hoc_phan['tenhp']}, Số tín chỉ: {hoc_phan['sotc']}")

def timchuoi(danhsach,chuoi):
    print(f"Các học phần có tên chứa chuỗi '{chuoi}': ")
    for hoc_phan in danhsach:
        if chuoi.lower() in hoc_phan["tenhp"].lower():
            print(f"Mã học phần: {hoc_phan['mahp']}, Tên học phần: {hoc_phan['tenhp']}, Số tín chỉ: {hoc_phan['sotc']}")


n = int(input("Nhập số lượng học phần (n < 10): "))
danhsach = []
for i in range(n):
    print(f"Nhập thông tin cho học phần thứ {i + 1}:")
    hoc_phan = nhap()
    danhsach.append(hoc_phan)

xuat(danhsach)

s = input("Nhập vào chuỗi tìm kiếm: ")
timchuoi(danhsach, s)
