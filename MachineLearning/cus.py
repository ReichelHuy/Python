import csv
import random
import string

# Số lượng khách hàng cần sinh
num_customers = 5000

# Tạo danh sách khách hàng
customers = []

for i in range(num_customers):
    # Sinh ngẫu nhiên CustomerID
    customer_id = 'KH' + ''.join(random.choices(string.digits, k=3))

    # Sinh ngẫu nhiên spend và Frequency
    spend = random.uniform(0, 500)
    frequency = random.randint(1, 10)

    # Thêm khách hàng vào danh sách
    customer = {'CustomerID': customer_id, 'spend': spend, 'Frequency': frequency}
    customers.append(customer)

# Tên các cột trong file CSV
fields = ['CustomerID', 'spend', 'Frequency']

# Tạo file CSV và ghi dữ liệu
with open('customer_data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    # Viết tiêu đề cột
    writer.writeheader()

    # Viết dữ liệu khách hàng
    writer.writerows(customers)

print("Đã tạo thành công tập tin 'customer_data.csv'")
