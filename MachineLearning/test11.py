import numpy as np
import matplotlib.pyplot as plt

# Dữ liệu chiều cao của các cây AVL và BST
AVL_heights = [23, 23, 23, 23, 23, 23, 23, 23, 23, 23]
BST_heights = [24, 25, 24, 24, 25, 24, 25, 24, 24, 24]

# Tạo list chứa các tên của các cây AVL và BST
tree_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
              '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# Tạo biểu đồ
plt.plot(tree_names[:10], AVL_heights, 'o', label='AVL', color='b')
plt.plot(tree_names[10:], BST_heights, 'o', label='BST', color='g')

# Tạo đường thẳng h=log2(10^6) và h1=1.45h
h = np.log2(10**6)
h1 = 1.45 * h
x = np.linspace(1, 10, 10)
y = np.full((10,), h)
y1 = np.full((10,), h1)
plt.plot(x, y, label=f'h={h:.2f}', linestyle='--', color='r')
plt.plot(x, y1, label=f'h1={h1:.2f}', linestyle='--', color='m')

# Nối tất cả các chấm cùng màu lại
plt.plot(tree_names[:10], AVL_heights, '-', color='b')
plt.plot(tree_names[10:], BST_heights, '-', color='g')

# Thiết lập giới hạn trục y
plt.ylim(0, 40)

# Đặt nhãn cho trục x và y
plt.xlabel('Test case')
plt.ylabel('Height of tree')

# Đặt tiêu đề cho biểu đồ
plt.title('Comparison of AVL and BST tree heights and two lines: h=log2(10^6) and h1=1.45h')

# Thêm chú thích
plt.legend()

# Hiển thị biểu đồ
plt.show()