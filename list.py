# cú pháp để khỏi tạo một danh sách là lst = [] 
lst = [2,3,4]
# thêm 1 phân tử vào mảng ta dùng phương thức append()
lst.append(5)
# danh sách có thể lưu nhiều kiểu dữ liệu khác nhau
lst.append("ICPC")
lst.append(False)
# câu lệnh print() cũng có thể áp dụng với danh sách
print(lst)

# XỬ LÝ CHUỖI
s="Nguyễn Quyết Tiến"
# hàm len() trả về kích thước của 1 chuỗi 
print(len(s))                       # 17
# phương thức lower() trả về chuỗi dạng in thường
print(s.lower())                    # nguyễn quyết tiến
# phương thức upper() trả về chuỗi dạng in hoa
print(s.upper())                    # NGUYỄN QUYẾT TIẾN
# phương thức isalnum() trả về true nếu xâu chỉ chứa các kí tự chữ hoặc số
print(s.isalnum())                  # False
# phương thức isalpha() trả về true nếu xâu chỉ chứa các kí tự chữ
print("tien".isalpha())             # True
# phương thức isnumeric() trả về true nếu xâu chỉ chứa các kí tự là số
print("0987675072".isnumeric())
#test


