import pandas as pd

# Đường dẫn và tên file Excel
path = r"C:/Users/DELL/Học tập AI k3/Học kỳ II/Phân tích dữ liệu Python/"
file_name = "Temperature.xlsx"

# Đọc file Excel vào DataFrame
data = pd.read_excel(path + file_name)

# Hiển thị một số hàng đầu của DataFrame
print("Một số hàng đầu của DataFrame:")
print(data.head())

# Xem thông tin về các cột và kiểu dữ liệu
print("\nThông tin về các cột và kiểu dữ liệu:")
print(data.info())

# Chọn các cột cần xem
selected_columns = ['Salinity', 'Temperature', 'Area', 'CHLFa', 'Month', 'Year', 'Season']
subset = data[selected_columns]

# Lọc dữ liệu (loại bỏ những dữ liệu không hợp lệ)
valid_data = subset.dropna()

# Mô tả dữ liệu
print("\nMô tả dữ liệu sau khi lọc:")
print(valid_data.describe())

# Trích xuất dữ liệu độ mặn của các năm 1990-1996, mùa summer và spring, và khu vực WZ
filtered_data = valid_data[(valid_data['Year'].between(1990, 1996)) & (valid_data['Season'].isin(['summer', 'spring'])) & (valid_data['Area'] == 'WZ')]
filtered_salinity = filtered_data['Salinity']

# Khám phá dữ liệu
print("\nDữ liệu độ mặn của các năm 1990-1996, mùa summer và spring, và khu vực WZ:")
print(filtered_salinity)

# Thống kê dữ liệu độ mặn
print("\nThống kê dữ liệu độ mặn:")
print(filtered_salinity.describe())

# Trực quan hóa dữ liệu độ mặn
filtered_salinity.plot(kind='hist', bins=10, title='Độ mặn')
