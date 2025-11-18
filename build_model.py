import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

print("Đang tải tệp articles.csv...")
# 1. Đọc dữ liệu từ tệp CSV
try:
    df = pd.read_csv("articles.csv")
except FileNotFoundError:
    print("LỖI: Không tìm thấy tệp 'articles.csv'.")
    print("Bạn hãy chắc chắn đã chạy tệp 'process_data.py' trước.")
    exit()

# Xử lý trường hợp có bài báo không cào được nội dung (NaN)
df['full_text'] = df['full_text'].fillna('')

print(f"Đã tải {len(df)} bài báo.")

# 2. Định nghĩa các Stopword Tiếng Việt cơ bản
# Đây là những từ phổ biến nhưng không có nhiều ý nghĩa
# Bạn có thể thêm nhiều từ hơn nếu muốn
vietnamese_stopwords = [
    "bị", "bởi", "cả", "các", "cái", "cần", "càng", "chỉ", "chiếc", "cho", "chứ", 
    "chưa", "có", "có thể", "cùng", "cũng", "đã", "đang", "đây", "để", "đến", 
    "đó", "được", "gì", "hay", "hết", "khi", "không", "là", "làm", "lại", "lên", 
    "lúc", "mà", "mỗi", "một", "này", "nên", "nếu", "ngay", "như", "nhưng", 
    "những", "nơi", "nữa", "phải", "qua", "ra", "rằng", "rất", "rồi", "sau", 
    "sẽ", "so", "sự", "tại", "theo", "thì", "trên", "trước", "từ", "từng", 
    "và", "vẫn", "vào", "vậy", "vì", "với", "vừa"
]

print("Bắt đầu Vector hóa TF-IDF...")
# 3. Khởi tạo TfidfVectorizer
# max_features=5000: Chỉ lấy 5000 từ quan trọng nhất
# stop_words: Loại bỏ các từ vô nghĩa
tfidf_vectorizer = TfidfVectorizer(max_features=5000, 
                                   stop_words=vietnamese_stopwords)

# 4. Huấn luyện và biến đổi cột 'full_text'
# .fit_transform() sẽ học từ vựng và biến đổi văn bản thành ma trận
tfidf_matrix = tfidf_vectorizer.fit_transform(df['full_text'])

print("Ma trận TF-IDF đã được tạo:")
print(f" - Số bài báo (hàng): {tfidf_matrix.shape[0]}")
print(f" - Số từ vựng (cột): {tfidf_matrix.shape[1]}")

# 5. Lưu kết quả để sử dụng sau
# Chúng ta lưu cả ma trận và vectorizer
with open("tfidf_model.pkl", "wb") as f_out:
    pickle.dump({
        "matrix": tfidf_matrix,
        "vectorizer": tfidf_vectorizer,
        "article_ids": df['article_id'].tolist() # Lưu cả danh sách ID
    }, f_out)

print("Đã lưu ma trận TF-IDF và Vectorizer vào tệp 'tfidf_model.pkl'.")
print("Hoàn thành Bước 2!")