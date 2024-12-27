sv = []

sinhvien = int(input("Nhập số lượng sinh viên: "))

for i in range(sinhvien):
    print(f"Nhập thông tin của sinh viên thứ {i + 1}: ")
    hoten = input("Họ và tên: ")
    masv = input("Nhập mã sv: ")
    ngaysinh = input("Nhập ngày tháng năm sinh: ")
    dtb = float(input("Nhập điểm trung bình: "))

    thong_tin = {
        'Họ tên': hoten,
        'Mã sinh viên': masv,
        'Ngày sinh': ngaysinh,
        'Điểm trung bình': dtb
     }

    #  Thêm sinh viên vào danh sách
    sv.append(thong_tin)

print("Danh sách sinh viên: ")
for sinh_vien in sv:
    if(dtb >= 8.0):
        print(f"Họ tên: {sinh_vien['Họ tên']}")
        print(f"Mã sinh viên: {sinh_vien['Mã sinh viên']}")
        print(f"Ngày sinh: {sinh_vien['Ngày sinh']}")
        print(f"Điểm trung bình: {sinh_vien['Điểm trung bình']}")
        print("\n")
        
