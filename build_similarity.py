import pickle
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

print("Đang tải tệp 'tfidf_model.pkl'...")
# 1. Tải tệp .pkl đã lưu ở bước trước
try:
    with open("tfidf_model.pkl", "rb") as f_in:
        model_data = pickle.load(f_in)
        
    tfidf_matrix = model_data["matrix"]
    article_ids = model_data["article_ids"]

except FileNotFoundError:
    print("LỖI: Không tìm thấy tệp 'tfidf_model.pkl'.")
    print("Bạn hãy chắc chắn đã chạy tệp 'build_model.py' trước.")
    exit()

print(f"Đã tải ma trận TF-IDF của {tfidf_matrix.shape[0]} bài báo.")

print("Bắt đầu tính toán Độ tương đồng Cosine (Cosine Similarity)...")
# 2. Tính toán ma trận tương đồng
# cosine_similarity() so sánh tất cả các hàng (bài báo) với nhau
cosine_sim_matrix = cosine_similarity(tfidf_matrix)

print("Đã tính toán xong ma trận tương đồng.")
print(f" - Kích thước ma trận: {cosine_sim_matrix.shape}")

# 3. Lưu ma trận tương đồng và danh sách ID vào tệp
# Lần này dùng định dạng .npz của Numpy để lưu trữ hiệu quả hơn
np.savez_compressed(
    "similarity_model.npz",
    matrix=cosine_sim_matrix,
    article_ids=article_ids
)

print("Đã lưu ma trận tương đồng vào tệp 'similarity_model.npz'.")
print("Hoàn thành Bước 3!")