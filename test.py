#1 Truy cập kí tự
def truycap():
    str = input("Nhập chuỗi bất kì: ")
    i = int(input("Nhập chỉ số của phần tử cần truy cập: "))
    print(f"Chuỗi '{str}' có phần tử str[{i}] là '{str[i]}'")


#2 Hàm nối 2 chuỗi
def connectstring():
    str1 = input("Nhập chuỗi 1: ")
    str2 = input("Nhập chuỗi 2: ")
    str = str1 +  str2
    print("Chuỗi sau khi nối: ", str)
    
#3 Hàm cắt chuỗi với vị trí chỉ định
def cutstring():
    str = input("Nhập xâu cần cắt: ")
    i = int(input("Vị trí bắt đầu: "))
    j = int(input("Vị trí kết thúc: "))
    str2 = str[i:j]
    print(f"Chuỗi sau khi cắt sẽ trở thành: '{str2}'")
    
#4 Sử dụng phương thức join ()  
def phuongthucjoin():
    print("Ví dụ:")
    print("str1 = 'Học'")
    print("str2 = 'Python'")
    print("str3 = 'rất'")
    print("str4 = 'vui'")
    str1 = "Học"
    str2 = "Python"
    str3 = "rất"
    str4 = "vui"
    str5 = input("Chuỗi cần chèn vào giữa các chuỗi trên: ")
    str = str5.join([str1, str2, str3, str4])
    print("Chuỗi mới sẽ là: ", str)
    
#5 Lặp chuỗi với số lần lặp là n
def lap():
    str = input("Nhập chuỗi lặp: ")
    n = int(input("Số lần lặp: "))
    print(str*n)
    
#6 Hàm tính độ dài
def lenstring():
    print("Thao tác tính độ dài của 1 chuỗi.")
    str = input("Nhập chuỗi: ")
    print(f"Chuỗi {str} có độ dài là ", len(str))

#7 Chuyển đổi chữ hoa
def chuhoa():
    str = input("Nhập chuỗi bất kì: ")
    strup = str.upper()
    print("Chuỗi sau khi chuyển đổi thành chữ hoa: ", strup)

#8 Chuyển đổi chữ thường
def chuthuong():
    str = input("Nhập chuỗi bất kì: ")
    strlow = str.lower()
    print("Chuỗi sau khi chuyển đổi thành chữ thường: ", strlow)

#9 Kiểm tra chuỗi con 
def ktchuoicon():
    str = input("Nhập chuỗi bất kì: ")
    strcon  = input("Nhập chuỗi con cần kiểm tra: ")
    if strcon in str:
        print(f"Chuỗi '{strcon}' có trong chuỗi '{str}'")
    else:
        print(f"Chuỗi '{strcon}' không có trong chuỗi '{str}'")
        
#10 Tách chuỗi thành các phần tử của 1 danh sách
def tachchuoi():
    str = input("Nhập chuỗi bất kì: ")
    char = input("Nhập kí tự ngăn cách giữa các từ cần tách: ")
    list = str.split(char)
    print(list)
        
#11 Thay thế 1 chuỗi bằng 1 chuỗi khác
def thaythe():
    str = input("Nhập chuỗi bất kì: ")
    str1 = input("Chuỗi cần thay thế: ")
    if str1 in str:
        str2 = input("Chuỗi thay thế: ")
        strreplace =  str.replace(str1, str2)
        print(f"Sau khi thay thế '{str1}' bằng '{str2}', chuỗi trở thành:  '{strreplace}'") 
    else:
        print(f"Chuỗi '{str1}' không có trong chuỗi '{str}'")        
        
#12 Xóa khoảng trắng thừa
def xoakhoangtrang():
    str = input("Nhập xâu cần xóa khoảng trắng: ")
    strclear = ' '.join(str.split())
    print("Xâu sau khi đã xóa các khoảng trắng thừa: ", strclear)
        
#13 Đảo ngược chuỗi
def daonguoc():
    str = input("Nhập chuỗi bất kì: ")
    str_reverse = str[::-1]
    print("Chuỗi sau khi đảo ngược: ", str_reverse)
        
#14 Kiểm tra chuỗi đối xứng
def check_symmetry():
    str = input("Nhập xâu cần kiểm tra: ")
    str_reserve = str[::-1]
    if str == str_reserve:
        print(f"Chuỗi {str} đối xứng!")
    else:
        print(f"Chuỗi {str} không đối xứng!")        
        
#15 In hoa chữ cái đầu tiên của mỗi từ
def inhoamoitu():
    str = input("Nhập chuỗi bất kì: ")
    str1 = str.title()
    print(f"Chuỗi {str} sẽ trở thành: ", str1)

#16 Đếm số lần xuất hiện của kí tự hoặc chuỗi trong một chuỗi khác
def dem():
    str = input("Nhập chuỗi bất kì: ")
    find = input("Nhập chuỗi hoặc kí tự cần đếm: ")
    n = int(str.count(find))
    print(f"'{find}' xuất hiện trong chuỗi '{str}' {n} lần! ")        

#17 Tìm vị trí xuất hiện đầu tiên của một chuỗi trong một chuỗi khác
def timvitrixuathien():
    str = input("Nhập chuỗi bất kì: ")
    str1 = input("Chuỗi cần tìm vị trí: ")
    if str1 in str:
        x = str.find(str1)
        print(f"Chuỗi '{str1}' xuất hiện đầu tiên ở vị trí '{x}' trong chuỗi '{str}'") 
    else:
        print(f"Chuỗi '{str1}' không có trong chuỗi '{str}'") 
        
#18 Căn chỉnh lề
def letrai():
    str = input("Nhập chuỗi bất kì: ")
    n = int(input("Độ rộng: "))
    char = input("Nhập kí tự cho khoảng trống: ")
    str1 = str.ljust(n,char)
    print("Kết quả:")
    print(str1)
def lephai():
    str = input("Nhập chuỗi bất kì: ")
    n = int(input("Độ rộng: "))
    char = input("Nhập kí tự cho khoảng trống: ")
    str1 = str.rjust(n,char)
    print("Kết quả:")
    print(str1)
def chinhgiua():
    str = input("Nhập chuỗi bất kì: ")
    n = int(input("Độ rộng: "))
    char = input("Nhập kí tự cho khoảng trống: ")
    str1 = str.center(n,char)
    print("Kết quả:")
    print(str1)
def canchinhle():
    print("1. Lề trái")
    print("2. Lề phải")
    print("3. Chính giữa")
    print("4. Thoát căn chỉnh lề")
    choose = int(input("Nhập tùy chọn: "))
    if choose == 1:
        letrai()
    elif choose == 2:
        lephai()
    elif choose == 3:
        chinhgiua()
    elif choose == 4:
        print("Đã thoát căn chỉnh lề!")

#19 Kiểm tra chuỗi
def kiemtrachuoi():
    print("1.Kiểm tra chữ số.")
    print("2.Kiểm tra chữ cái.")
    print("3.Kiểm tra chuỗi rỗng.")
    print("4.Kiểm tra chữ in hoa.")
    print("5.Kiểm tra chữ in thường.")
    print("6.Kiểm tra chuỗi chỉ chứa chữ cái và số.")
    print("7.Kiểm tra chuỗi có dạng titlecase.")
    print("8.Thoát kiểm tra chuỗi.")
    choose  = int(input("Nhập tùy chọn: "))
    
    if choose == 1:
        str = input("Nhập chuỗi cần kiểm tra: ")
        if str.isdigit():
            print(f"'{str}' là chữ số!")
        else:
            print(f"'{str}'không phải chữ số!")
    elif choose == 2:
        str = input("Nhập chuỗi cần kiểm tra: ")
        if str.isalpha():
            print(f" '{str}' là chữ cái!")
        else:
            print(f"'{str}'không phải chữ cái!")
    elif choose == 3:
        str = input("Nhập chuỗi cần kiểm tra: ")
        if str.isspace():
            print(f"'{str}' là chuỗi rỗng!")
        else:
            print(f"'{str}' không phải chuỗi rỗng!")
    elif choose == 4:
        str = input("Nhập chuỗi cần kiểm tra: ")
        if str.isupper():
            print(f"'{str}' là chữ in hoa!")
        else:
            print(f"'{str}' không phải chữ in hoa!")
    elif choose == 5:
        str = input("Nhập chuỗi cần kiểm tra: ")
        if str.islower():
            print(f"'{str}' là chữ in thường!")
        else:
            print(f"'{str}' không phải chữ in thường!")
    elif choose == 6:
        str = input("Nhập chuỗi cần kiểm tra: ")
        if str.isalnum():
            print(f"'{str}' chỉ chứa chữ cái và số!")
        else:
            print(f"'{str}' không chỉ chứa chữ cái và số!")
    elif choose == 7:
        str = input("Nhập chuỗi cần kiểm tra: ")
        if str.istitle():
            print(f"'{str}' có dạng titlecase!")
        else:
            print(f"'{str}' không có dạng titlecase!")
    elif choose == 8:
        print("Đã thoát kiểm tra chuỗi!")

#20 Tính tổng các chữ số trong chuỗi
def tongchuso():
    sum = 0
    str = input("Nhập chuỗi cần tính")  
    for x in str:
        if x.isdigit():
            sum += int(x)
    print(f"Tổng các chữ số trong chuỗi '{str}' là {sum}")

#21 Tách chữ cái và số
def tachchucaivaso():
    alpha = ""
    digit = ""
    str = input("Nhập chuỗi cần tách: ")
    for x in str:
        if x.isdigit():
            digit += x
        elif x.isalpha():
            alpha += x
    print(f"'{str}' sau khi tách sẽ gồm: ")
    print("Số: ", digit)
    print("Chữ cái: ", alpha)

# Hàm hiển thị menu
def show_menu():
    print("ĐỀ TÀI NHÓM".center(69,'-'))
    print("1. Truy cập kí tự.")
    print("2. Nối hai chuỗi.")
    print("3. Cắt chuỗi với vị trí chỉ định.")
    print("4. Chèn 1 chuỗi vào giữa nhiều chuỗi khác.")
    print("5. Lặp chuỗi với số lần lặp xác định.")
    print("6. Tính độ dài chuỗi.")
    print("7. Chuyển đổi chữ hoa.")
    print("8. Chuyển đổi chữ thường.")
    print("9. Kiểm tra chuỗi con.")
    print("10. Tách chuỗi thành các phần tử của 1 danh sách.")
    print("11. Thay thế 1 chuỗi bằng 1 chuỗi khác.")
    print("12. Xóa khoảng trắng thừa.")
    print("13. Đảo ngược chuỗi.")
    print("14. Kiểm tra chuỗi đối xứng.")
    print("15. In hoa chữ cái đầu tiên của mỗi từ.")
    print("16. Đếm số lần xuất hiện của kí tự hoặc chuỗi trong một chuỗi khác.")
    print("17. Tìm vị trí xuất hiện đầu tiên của một chuỗi trong một chuỗi khác.")
    print("18. Căn chỉnh lề.")
    print("19. Kiểm tra chuỗi.")
    print("20. Tính tổng các chữ số.")
    print("21. Tách chữ cái và số.")
    print("22. Thoát khỏi chương trình. ")  
    
# Hàm thực thi lệnh
def execute_command(cmd):
    if cmd == 1:
        clear_console()
        print("Bạn đã chọn thao tác truy cập kí tự! ")
        truycap()
    elif cmd == 2:
        clear_console()
        print("Bạn đã chọn thao tác nối hai chuỗi!")
        connectstring()
    elif cmd == 3:
        clear_console()
        print("Bạn đã chọn thao tác cắt chuỗi với vị trí chỉ định!")
        cutstring()
    elif cmd == 4: 
        clear_console()
        print("Bạn đã chọn thao tác chèn 1 chuỗi vào giữa nhiều chuỗi khác!")
        phuongthucjoin()
    elif cmd == 5: 
        clear_console()
        print("Bạn đã chọn thao tác lặp chuỗi với số lần lặp xác định!")
        lap()
    elif cmd == 6: 
        clear_console()
        print("Bạn đã chọn thao tác tính độ dài chuỗi!")
        lenstring()
    elif cmd == 7: 
        clear_console()
        print("Bạn đã chọn thao tác chuyển đổi chữ hoa!")
        chuhoa()
    elif cmd == 8:
        clear_console() 
        print("Bạn đã chọn thao tác chuyển đổi chữ thường!")
        chuthuong()
    elif cmd == 9: 
        clear_console()
        print("Bạn đã chọn thao tác kiểm tra chuỗi con!")
        ktchuoicon()
    elif cmd == 10: 
        clear_console()
        print("Bạn đã chọn thao tác tách chuỗi thành các phần tử của 1 danh sách!")
        tachchuoi()
    elif cmd == 11:
        clear_console() 
        print("Bạn đã chọn thao tác thay thế 1 chuỗi bằng 1 chuỗi khác!")
        thaythe()
    elif cmd == 12: 
        clear_console()
        print("Bạn đã chọn thao tác xóa khoảng trắng thừa!")
        xoakhoangtrang
    elif cmd == 13: 
        clear_console()
        print("Bạn đã chọn thao tác đảo ngược chuỗi!")
        daonguoc()
    elif cmd == 14: 
        clear_console()
        print("Bạn đã chọn thao tác kiểm tra chuỗi đối xứng!")
        check_symmetry()
    elif cmd == 15: 
        clear_console()
        print("Bạn đã chọn thao tác in hoa chữ cái đầu tiên của mỗi từ!")
        inhoamoitu()
    elif cmd == 16: 
        clear_console()
        print("Bạn đã chọn thao tác dếm số lần xuất hiện của kí tự hoặc chuỗi trong một chuỗi khác!")
        dem()
    elif cmd == 17: 
        clear_console()
        print("Bạn đã chọn thao tác tìm vị trí xuất hiện đầu tiên của một chuỗi trong một chuỗi khác!")
        timvitrixuathien()
    elif cmd == 18: 
        clear_console()
        print("Bạn đã chọn thao tác căn chỉnh lề!")
        canchinhle()
    elif cmd == 19: 
        clear_console()
        print("Bạn đã chọn thao tác kiểm tra chuỗi!")
        kiemtrachuoi()
    elif cmd == 20: 
        clear_console()
        print("Bạn đã chọn thao tác tính tổng các chữ số!")
        tongchuso()
    elif cmd == 21: 
        clear_console()
        print("Bạn đã chọn thao tác tách chữ cái và số!")
        tachchucaivaso()
    elif cmd == 22:
        clear_console()
        print("Đã dừng chương trình!") 
    
import os
def clear_console():
    command = 'cls'  # Sử dụng 'cls' cho Windows
    os.system(command)

# Chương trình chính        
command = 0    
while True:
    show_menu()
    command = int(input("Nhập tùy chọn của bạn: "))
    execute_command(command)
    if command == 22:
        break
    