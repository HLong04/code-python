def string_S():
    while True:
        print("--------------- Chọn ---------------")
        print("1. Xác định độ dài chuỗi ")
        print("2. Cắt chuỗi ")
        print("3. Chuyển đổi sang chữ hoa ")
        print("4. Chuyển đổi sang chữ thường ")
        print("5. Viết hoa chữ cái đầu tiên ")
        print("6. Loại bỏ khoảng trắng du thừa ")
        print("7. Cộng hai chuổi lại với nhau ")
        print("8. Truy cầp ký tự ")
        print("9. Lặp đi lặp lại nhiều lần ")
        print("Nhất 0 để kết thúc chương trình!")
    
    # Nhập chuỗi từ bàn phím
        s = int(input("Nhập số ban muốn: "))

        if s == 0:
            print("Kết thúc chương trình!")
            break

        if 1 <=  s <= 9:

    # 1. Xác định độ dài chuỗi     
            if(s == 1):
                a = input("Nhập chuổi cần giải quyết: ")
                do_dai = len(a)
                print(f"Độ dài chuỗi: {do_dai}")

    # 2. Cắt chuỗi (lấy các ký tự từ 2 đến 5)
            elif(s == 2):
                a = input("Nhập chuổi cần giải quyết: ")
                bentrai = int(input("Nhập số cần cắt bên trái: "))
                benphai = int(input("Nhập số cần cắt bên phải : "))
                cat_chuoi = a[bentrai:benphai]
                print(f"Chuỗi con cắt {bentrai} và {benphai}: {cat_chuoi}")

    # 3, 4, 5:  Chuyển đổi sang chữ hoa hoặc chữ thường và viết hoa chữ cái đầu
            elif(s == 3):
                a = input("Nhập chuổi cần giải quyết: ")
                hoa = a.upper()
                print(f"Chữ hoa: {hoa}")
    
            elif(s == 4):
                a = input("Nhập chuổi cần giải quyết: ")
                thuong = a.lower()
                print(f"Chữ thường: {thuong}")
            
            elif(s == 5):
                a = input("Nhập chuổi cần giải quyết: ")
                hoadaucau = viethoa(a)
                print(f"Viết hoa tất cả chữ cái đầu: {hoadaucau}")

    # 6. Loại bỏ khoảng trắng du thừa
            elif(s == 6):
                a = input("Nhập chuỗi cần giải quyết: ")
                xoakhoangtrang = ' '.join(a.strip().split())
                print(f"Chuỗi sau khi xoá khoảng trống dư thừa: '{xoakhoangtrang}'")


    # 7. Cộng hai chuổi lại với nhau
            elif(s == 7):
                a =input("Nhập chuổi thứ nhất: ")
                b = input("Nhập chuổi thứ hai: ")
                concat = a + " " + b
                print(f"Chuỗi đã gộp lại: {concat}")
            
    #8. Truy cập ký tự 
            elif(s == 8): 
                a = input("Nhập chuổi cần giải quyết: ")
                index = int(input("Nhập vị trí muốn truy cập: "))
                print(f"Chuỗi {a} ở số {index} là: {a[index]}")
    #9. vòng lặp
            elif(s==9):
                a = input("Nhập chuỗi cần giải quyết: ")
                n = int(input("Số lần lặp: "))
                for i in range(0,n):
                    print(a)
    #10. 
        else:
            print("Nhập lại!!!")

def viethoa(a):
    return a.title()

string_S()
