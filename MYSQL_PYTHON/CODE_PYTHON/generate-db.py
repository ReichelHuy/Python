# Import libraries
import pymysql # conect ,commit mysql sever 
import random  # generate random number
from faker import Faker # support random fake infomation 
def generateDB(database_name): 
    # Connect databases
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Maytinh1',
        db=database_name,
        charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
                                )   
    # Cursor object 
    cursor = connection.cursor()
    # Generate data for TRUONG table
    faker = Faker('vi_VN')
    for i in range(100):
        ten_tr = faker.company() #Fake name company
        dia_chi_tr = faker.address() #Fake address
        cursor.execute("INSERT INTO TRUONG (TEN_TR, DIA_CHI_TR) VALUES (%s, %s)", (ten_tr, dia_chi_tr)) #Insert Value 

    connection.commit() # Commit 

    # Generate data for HS table
    for i in range(1000000):    # 1mil student 
        ho = faker.first_name() # Fake first name
        ten = faker.last_name() # Fake last name
        cccd = faker.unique.random_number(digits=12)    #Fake cccd, unique , 12 digit for each
        ntns = faker.date_of_birth()    #fake birth
        dchi_hs = faker.address()       #fake address
        cursor.execute("INSERT INTO HS (HO, TEN, CCCD, NTNS, DCHI_HS) VALUES (%s, %s, %s, %s, %s)", (ho, ten, cccd, ntns, dchi_hs))

    connection.commit()

    # Generate data for HOC table
    for i in range(1000000):           # Generate 1mil info
        ma_tr = random.randint(1, 100) # Generate random number
        ma_hs = i + 1                  # ma_hs is unique, 1->1mil, no ramdom 
        namhoc = random.randint(2000, 2022) # Random
        diemtb = round(random.uniform(0, 10), 2)    #Random up to 1/100
        if diemtb >= 9:
            xeploai = 'Xuat sac'
        if diemtb >= 8:
            xeploai = 'Gioi'
        elif diemtb >= 6.5:
            xeploai = 'Kha'
        elif diemtb >= 5:
            xeploai = 'Trung binh'
        else:
            xeploai = 'Yeu'
        kqua = 'Hoan thanh' if diemtb >= 5 else 'Chua hoan thanh'
        cursor.execute("INSERT INTO HOC (MA_TR, MA_HS, NAMHOC, DIEMTB, XEPLOAI, KQUA) VALUES (%s, %s, %s,%s, %s, %s)", (ma_tr, ma_hs, namhoc, diemtb, xeploai, kqua))
    
    connection.commit()
    # Close connection
    connection.close()
    
# Using 
generateDB('TRUONGHOC1')

