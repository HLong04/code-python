def nhap():
    n = int(input("Nhập số lần nhập thông tin sinh viên: "))
    sv = []
    
    for i in range(n):
        msv = input("Nhập mã sinh viên: ")

        hoten = input("Nhập họ và tên: ")
        hoadaucau = viethoa(hoten)

        dtb = float(input("Nhập điểm trung bình: "))
        diem = xeploai(dtb)
        
        sv.append((msv, hoadaucau, dtb,diem)) 

    return sv

def xeploai(dtb):
    if 8.0 <= dtb <= 10.0:
        return " Loại Giỏi"
    elif 6.5 <= dtb < 8.0:
        return " Loại Khá"
    elif 4.0 <= dtb < 6.5:
        return " Loại Trung bình"
    elif dtb < 4.0:
        return " Loại Yếu"
    else:
        return " Loại Kém"
    
def viethoa(hoten):
    return hoten.title() 

def xuat(msv, hoten, dtb,diem,dem):
    print("\n----------------------------------------------------\n")
    print(f"Danh sách sinh viên thứ {dem+1}: ")
    print("Mã sinh viên: ", msv)
    print("Họ tên sinh viên: ", hoten)
    print("Điểm trung bình: ", dtb , diem)

a = nhap()
for dem,student in enumerate(a):
    xuat(*student,dem = dem)
