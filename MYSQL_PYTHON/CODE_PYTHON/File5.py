import pandas as pd
import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Maytinh1',
    db='TRUONGHOC',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
# Tạo đối tượng cursor để thực thi các câu lệnh SQL
cursor = connection.cursor()
# Đọc file excel và lấy dữ liệu từ sheet có tên "Sheet1"
df = pd.read_excel('/Users/duynguyendinh/Downloads/coderun/python/MySQL_PYTHON/Data/file_daotao_5.xlsx', sheet_name='Sheet1')
#-----giá trị của các key_value
# value_key = df.iloc[3, :7].values
# print(value_key)
#-----giá trị của file excel
# keys = df.iloc[3:, :7].values.flatten().tolist()
# print(excel
#-----giá trị của các row
# 0: mã trường, 1 :tên trường, 2: sở GD&ĐT, 3: Phòng ,4:loại hình, 5 loại trường,6Địa_chỉ
# Chú ý, bắt đầu từ hàng 4 đổ xuống tức là 3:
#-----các row--------
loai_hinh = df.iloc[3:,4]
loai_truong = df.iloc[3:,5]
phong_gd = df.iloc[3:,3]
ma_truong = df.iloc[3:,0].values.flatten().tolist()
ten_truong= df.iloc[3:,1].values.flatten().tolist()
so_gddt= df.iloc[3:,2]
dia_chi= df.iloc[3:,6].values.flatten().tolist()

#----------Loai_hinh_id-------------------
loai_hinh_id = []
for index, value in loai_hinh.items():
    # Tìm ID tương ứng của loại hình trong bảng LOAI_HINH
    if pd.isna(value):
        query = "SELECT ID FROM LOAI_HINH WHERE TEN_LOAI_HINH IS NULL"
    else:
        query = "SELECT ID FROM LOAI_HINH WHERE TEN_LOAI_HINH='{}'".format(value)
    cursor.execute(query)
    result = cursor.fetchone()
    if result is not None:
        loai_hinh_id.append(result['ID'])
#print(loai_hinh_id)


#--------Loai_truong_id------------------
loai_truong_id =[]
for index, value in loai_truong.items():
    # Tìm ID tương ứng của loại trường trong bảng LOAI_TRUONG
    if pd.isna(value):
        query = "SELECT ID FROM LOAI_HINH WHERE TEN_LOAI_HINH IS NULL"
    else:
        query = "SELECT ID FROM LOAI_TRUONG WHERE TEN_LOAI_TRUONG='{}'".format(value)
    cursor.execute(query)
    result = cursor.fetchone()
    if result is not None:
        loai_truong_id.append(result['ID'])
    else:
        query= "SELECT ID FROM LOAI_TRUONG WHERE TEN_LOAI_TRUONG='Khác'"
        cursor.execute(query)
        result = cursor.fetchone()
        loai_truong_id.append(result['ID'])
#print(loai_truong_id)

#-------------phond_gd_id--------------------
phong_gd_id=[]
for index, value in phong_gd.items():
    # Tìm ID tương ứng của phòng GDĐT trong bảng PH_GDDT
    if pd.isna(value):
        query = "SELECT ID FROM PH_GDDT WHERE TEN_PH_GDDT IS NULL"
    else:
        query = "SELECT ID FROM PH_GDDT WHERE TEN_PH_GDDT='{}'".format(value)
    cursor.execute(query)
    result= cursor.fetchone()
    if result is not None:
        phong_gd_id.append(result['ID'])
#print(phong_gd_id)

     # Tạo ra câu lệnh insert into từ dữ liệu và ID tương ứng
insert_commands = []
for i in range(len(ma_truong)):
   insert_command = "INSERT INTO TH_TIN_CHUNG (MaTruong, TenTruong, Dia_Chi, Loai_Hinh_ID, Loai_Truong_ID, Phong_GD_ID) VALUES ('{}', '{}', '{}', {}, {}, {})".format(ma_truong[i], ten_truong[i], dia_chi[i], loai_hinh_id[i], loai_truong_id[i], phong_gd_id[i])
   insert_commands.append(insert_command)
 #  cursor.execute(insert_command)
query = "UPDATE TH_TIN_CHUNG SET SoGD='Sở Giáo dục và đào tạo thành phố HCM'"
cursor.execute(query)
connection.commit()    
connection.close()
#print(insert_commands)

# Mở file mới để ghi các câu lệnh INSERT INTO vào
with open('Query5.txt', 'w') as f:
    #Xoá sạch trước khi ghi
    f.truncate()
    # Duyệt qua danh sách các câu lệnh và ghi vào file
    for command in insert_commands:
        f.write(command + ';' +'\n')

# Đóng file sau khi ghi xong
f.close()