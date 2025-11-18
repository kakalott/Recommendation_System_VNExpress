import pickle
import pandas as pd
import numpy as np

# Số lượng hàng (bài báo) và cột (từ) bạn muốn hiển thị
NUM_ROWS_TO_SHOW = 10
NUM_COLS_TO_SHOW = 100

print("Đang tải mô hình TF-IDF và dữ liệu bài báo...")
try:
    # Tải tệp CSV
    df_articles = pd.read_csv("articles.csv")
    
    # Tải tệp .pkl (từ Bước 2)
    with open("tfidf_model.pkl", "rb") as f_in:
        model_data = pickle.load(f_in)
        
    tfidf_matrix = model_data["matrix"]
    vectorizer = model_data["vectorizer"]
    
except FileNotFoundError:
    print("LỖI: Không tìm thấy tệp 'articles.csv' hoặc 'tfidf_model.pkl'.")
    print("Hãy chắc chắn bạn đang chạy script này trong cùng thư mục dự án.")
    exit()

print("Mô hình đã được tải.")

# 1. Lấy tên của tất cả 5000 từ (cột)
all_feature_names = vectorizer.get_feature_names_out()

# 2. Lấy 5 hàng đầu tiên của ma trận
first_5_rows_sparse = tfidf_matrix[0:NUM_ROWS_TO_SHOW]

# 3. Chuyển 5 hàng này sang ma trận đặc (dense)
first_5_rows_dense = first_5_rows_sparse.toarray()

# 4. Tạo DataFrame cho 5 hàng này
df_5_rows = pd.DataFrame(first_5_rows_dense, columns=all_feature_names)

# 5. Tìm 10 cột (từ) có giá trị TF-IDF trung bình cao nhất
# Điều này giúp chúng ta chọn ra các "từ khóa" quan trọng nhất
top_features_indices = df_5_rows.mean().nlargest(NUM_COLS_TO_SHOW).index
df_snippet = df_5_rows[top_features_indices]

# 6. Làm tròn số để dễ nhìn
df_snippet = df_snippet.round(4)

# 7. Thêm cột tiêu đề bài báo vào để dễ so sánh
titles = df_articles.head(NUM_ROWS_TO_SHOW)[['article_id', 'title']]
final_df = pd.concat([titles.reset_index(drop=True), df_snippet.reset_index(drop=True)], axis=1)

# 8. Lưu ra tệp CSV
output_filename = "matrix_for_presentation.csv"
final_df.to_csv(output_filename, index=False, encoding="utf-8-sig")

print("\nHOÀN TẤT!")
print(f"Đã tạo thành công tệp '{output_filename}'.")
print("\nBảng xem trước của bạn:")
print(final_df.head())