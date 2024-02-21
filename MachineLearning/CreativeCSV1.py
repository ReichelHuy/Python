import pandas as pd

data = pd.DataFrame({'text': ['This is the first document.',
                              'This document is the second document.',
                              'And this is the third one.',
                              'Is this the first document?'],
                     
                     'phrase': ['This is', 'third document', 'third one', 'second document'],
                     
                     'label': [1, 0, 1, 0]}
                    
                    )

# Tạo DataFrame từ dữ liệu
df = pd.DataFrame(data)

# Lưu DataFrame thành tệp CSV
df.to_csv('text1.csv', index=False)