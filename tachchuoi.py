def tachchuoi(string):
    # Tách ngày, tháng, và năm từ chuỗi
    date, month, year = [int(partial) for partial in string.split('/')]
    return date, month, year

date_string_start = input('Nhập ngày bắt đầu (DD/MM/YYYY): ')
date_string_end = input('Nhập ngày kết thúc (DD/MM/YYYY): ')

date_start, month_start, year_start = tachchuoi(date_string_start)
date_end, month_end, year_end = tachchuoi(date_string_end)

# Tính toán khoảng cách giữa các ngày
date_distance = (year_end - year_start) * 365 + (month_end - month_start) * 30 + (date_end-date_start)

print("Khoảng cách giữa các ngày (theo số ngày):", date_distance, "ngày")