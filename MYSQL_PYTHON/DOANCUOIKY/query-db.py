import pymysql
import time # lib calculate execute time in seconds
import xml.etree.ElementTree as ET


#Function 
def query_data(database_name, ten_truong, nam_hoc, xep_loai): #Access database
    # Connect to database
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Maytinh1',
        db=database_name,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    cursor = connection.cursor()

    # Query data
    start_time = time.time() #calculate time

    cursor.execute("""
        SELECT HS.HO, HS.TEN, HS.NTNS, HOC.DIEMTB, HOC.XEPLOAI, HOC.KQUA
        FROM HOC
        INNER JOIN HS ON HOC.MA_HS = HS.MA_HS
        INNER JOIN TRUONG ON HOC.MA_TR = TRUONG.MA_TR
        WHERE TRUONG.TEN_TR = %s AND HOC.NAMHOC = %s AND HOC.XEPLOAI = %s
    """, (ten_truong, nam_hoc, xep_loai))

    results = cursor.fetchall() # Get result

    end_time = time.time()  # Get time

    # Print results on terminal
    print("Danh sách học sinh:")
    for result in results: # Result output: Type ['HO':Data], ...
        ho_ten = result['HO'] + ' ' + result['TEN'] 
        ntns = result['NTNS'].strftime('%d/%m/%Y')
        diem_tb = result['DIEMTB']
        xep_loai_hs = result['XEPLOAI']
        ket_qua = result['KQUA']
        print(f"- {ho_ten}, {ntns}, {diem_tb}, {xep_loai_hs}, {ket_qua}") #print result

    # Export data to XML file
    xml_filename = f"XML/{database_name}-{ten_truong}-{nam_hoc}-{xep_loai}.xml" #create xml file
    root = ET.Element("students") # origin tag

    for result in results:
        student = ET.SubElement(root, "student")    #Result output
        ho_ten = result['HO'] + ' ' + result['TEN']
        ntns = result['NTNS'].strftime('%d/%m/%Y')
        diem_tb = str(result['DIEMTB'])
        xep_loai_hs = result['XEPLOAI']
        ket_qua = result['KQUA']

        ET.SubElement(student, "ho_ten").text = ho_ten  #create Subtag
        ET.SubElement(student, "ntns").text = ntns
        ET.SubElement(student, "diem_tb").text = diem_tb
        ET.SubElement(student, "xep_loai").text = xep_loai_hs
        ET.SubElement(student, "ket_qua").text = ket_qua

    xml_string = ET.tostring(root, encoding="unicode", method="xml")
    xml_string = xml_string.replace("><", ">\n    <")
    xml_string = xml_string.replace("student>\n    <student", "student>\n<student")
    xml_string = xml_string.replace("    </student>", "</student>")
    xml_string = xml_string.replace("    <student>", "<student>")
    xml_string = xml_string.replace("<students>", "    <students>")
    with open(xml_filename, 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write(xml_string)
       
    # Close connection
    connection.close()

    # Print query time
    query_time = end_time - start_time
    print(f"Thời gian truy vấn: {query_time:.3f} giây") # Round 1/1000

#Input
database_name = input("Nhập tên database: ")
ten_truong = input("Nhập tên trường: ")
nam_hoc = int(input("Nhập năm học: "))
xep_loai = input("Nhập xếp loại: ")

query_data(database_name, ten_truong, nam_hoc, xep_loai)

# Example usage
#query_data("TRUONGHOC1", "Johnston LLC", 2022, "Kha")
# Example usage
#query_data("TRUONGHOC2", "Johnston LLC", 2022, "Kha")