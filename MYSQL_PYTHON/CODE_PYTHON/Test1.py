
import pandas as pd
import mysql.connector

# Kết nối đến cơ sở dữ liệu MySQL
db = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)
cursor = db.cursor()

# Chèn dữ liệu vào bảng TT_CHUNG từ các file Excel
for i in range(1, 5):
    file_name = f"file_daotao_{i}.xlsx"
    df = pd.read_excel(file_name)
    for index, row in df.iterrows():
        ma_loai_truong = row["Mã Trường"]
        loai_truong = row["Loại Trường"]
        so_giao_duc_dao_tao = row["Sở GD&ĐT"]
        phong_gddt = row["Phòng GD&ĐT"]
        query = f"INSERT INTO TT_CHUNG (Ma_Loai_Truong, Loai_Truong, So_Giao_Duc_Dao_Tao, PhongGDDT) VALUES ('{ma_loai_truong}', '{loai_truong}', '{so_giao_duc_dao_tao}', '{phong_gddt}')"
        cursor.execute(query)
        db.commit()

# Chèn dữ liệu vào bảng TT_RIENG từ các file Excel
for i in range(1, 5):
    file_name = f"file_daotao_{i}.xlsx"
    df = pd.read_excel(file_name)
    for index, row in df.iterrows():
        ma_truong = row["Mã trường"]
        ten_truong = row["Tên trường"]
        dia_chi = row["Địa chỉ"]
        query = f"INSERT INTO TT_RIENG (Ma_Truong, Ten_Truong, DiaChi) VALUES ('{ma_truong}', '{ten_truong}', '{dia_chi}')"
        cursor.execute(query)
        db.commit()

# Chèn dữ liệu vào bảng TT_DAOTAO từ các file Excel
for i in range(1, 5):
    file_name = f"file_daotao_{i}.xlsx"
    df = pd.read_excel(file_name)
    for index, row in df.iterrows():
        ma_truong = row["Mã Trường"]
        ma_loai_truong = row["Ma_Loai_Truong"]
        loai_hinh = row["Loại hình"]
        query = f"INSERT INTO TT_DAOTAO (Ma_Truong, Ma_Loai_Truong, Loai_Hinh) VALUES ('{ma_truong}', '{ma_loai_truong}', '{loai_hinh}')"
        cursor.execute(query)
        db.commit()
  
# Đóng kết nối đến cơ sở dữ liệu MySQL
db.close()