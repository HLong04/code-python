def tinh_xac_suat(chuoi_van_ban):
    tu_khong_phan_biet_chu_hoa = chuoi_van_ban.lower().split() 
    tong_so_tu = len(tu_khong_phan_biet_chu_hoa) 
    xac_suat_dict = {} 
    for tu in tu_khong_phan_biet_chu_hoa: 
        if tu in xac_suat_dict: 
            xac_suat_dict[tu] += 1 
        else: xac_suat_dict[tu] = 1 
        for tu, so_lan_xuat_hien in xac_suat_dict.items(): 
            xac_suat = (so_lan_xuat_hien / tong_so_tu) * 100 
            print(f'p({tu}): {xac_suat:.2f}%') 
            
# Nhập văn bản từ người dùng 
van_ban = input("Nhập chuỗi văn bản: ") 

# Tính và in xác suất xuất hiện của từng từ trong văn bản 
tinh_xac_suat(van_ban)