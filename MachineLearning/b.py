import matplotlib.pyplot as plt
import seaborn as sns

# Tạo DataFrame từ dữ liệu đã chuẩn hóa
df_train_scaled = pd.DataFrame(X_train_scaled, columns=X_train.columns)

# Biểu đồ boxplot trước và sau khi chuẩn hóa
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
sns.boxplot(data=X_train, ax=axes[0])
axes[0].set_title('Trước khi chuẩn hóa')
sns.boxplot(data=df_train_scaled, ax=axes[1])
axes[1].set_title('Sau khi chuẩn hóa')
plt.show()

# Biểu đồ phân phối trước và sau khi chuẩn hóa
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
for feature in X_train.columns:
    sns.kdeplot(X_train[feature], ax=axes[0])
axes[0].set_title('Trước khi chuẩn hóa')
for feature in df_train_scaled.columns:
    sns.kdeplot(df_train_scaled[feature], ax=axes[1])
axes[1].set_title('Sau