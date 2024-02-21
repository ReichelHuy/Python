import xml.etree.ElementTree as ET
import os

def print_data_from_xml(xml_filename, a, b):
    # Parse XML file
    # Di chuyển đến thư mục XML
    os.chdir('XML')
    tree = ET.parse(xml_filename)
    root = tree.getroot()

    # Print data
    print(f"Danh sách học sinh với điểm trung bình từ {a} đến {b}:")
    for student in root.findall("./student"):
        ho_ten = student.find("ho_ten").text    #find all subtag
        diem_tb = float(student.find("diem_tb").text)
        if a <= diem_tb <= b:
            ntns = student.find("ntns").text
            xep_loai_hs = student.find("xep_loai").text
            ket_qua = student.find("ket_qua").text
            print(f"- {ho_ten}, {ntns}, {diem_tb}, {xep_loai_hs}, {ket_qua}")
       
        
# Example usage
# xml_filename = "TRUONGHOC1-Johnston LLC-2022-Gioi.xml"
# a = 8.0
# b = 8.3
xml_filename = input("Nhập tên tệp tin XML(lưu ý phải có duôi .xml): ")
a = float(input("Nhập điểm bắt đầu: "))
b = float(input("Nhập điểm kết thúc: "))

print_data_from_xml(xml_filename, a, b)