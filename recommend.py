import pandas as pd
import numpy as np
import sys

# 1. Tải các mô hình đã lưu
try:
    # Tải ma trận tương đồng (kết quả từ Bước 3)
    model_data = np.load("similarity_model.npz")
    cosine_sim_matrix = model_data["matrix"]
    all_article_ids = model_data["article_ids"]
    
    # Tải tệp CSV (kết quả từ Bước 1) để lấy tiêu đề
    df_articles = pd.read_csv("articles.csv")
    
    # Tạo một "ánh xạ" từ article_id -> title
    id_to_title = pd.Series(df_articles.title.values, index=df_articles.article_id).to_dict()

except FileNotFoundError:
    print("LỖI: Không tìm thấy tệp 'similarity_model.npz' hoặc 'articles.csv'.")
    print("Hãy chạy 'build_model.py' và 'build_similarity.py' trước.")
    exit()

def get_recommendations(article_id, num_recommendations=5):
    """
    Hàm chính để lấy khuyến nghị
    """
    
    # 2. Lấy chỉ số (index) của bài báo trong ma trận
    try:
        # Lấy vị trí (index) của bài báo trong danh sách
        idx = np.where(all_article_ids == article_id)[0][0]
    except IndexError:
        print(f"LỖI: Không tìm thấy bài báo với ID '{article_id}'")
        return

    # 3. Lấy hàng tương đồng của bài báo đó
    # sim_scores là một danh sách điểm tương đồng của bài báo 'idx' với TẤT CẢ các bài khác
    sim_scores = list(enumerate(cosine_sim_matrix[idx]))

    # 4. Sắp xếp các bài báo dựa trên điểm tương đồng
    # Sắp xếp theo điểm số (phần tử thứ 1), lấy từ cao đến thấp (reverse=True)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # 5. Lấy 5 bài báo có điểm cao nhất
    # Bắt đầu từ 1 (bỏ qua bài đầu tiên, vì đó chính là nó)
    top_scores = sim_scores[1 : num_recommendations + 1]

    # Lấy ID của các bài báo đó
    recommended_indices = [i[0] for i in top_scores]
    recommended_ids = [all_article_ids[i] for i in recommended_indices]
    
    # 6. Trả về kết quả
    return recommended_ids

# --- MAIN ---
if __name__ == "__main__":
    # Lấy ID bài báo từ dòng lệnh
    if len(sys.argv) > 1:
        input_id = sys.argv[1]
    else:
        # Nếu không, dùng một ID mẫu
        # Bạn có thể thay ID này bằng bất kỳ ID nào trong tệp articles.csv
        input_id = "thoi-su_url_316" 
        print(f"Không có ID nào được nhập. Dùng ID mẫu: {input_id}")

    print("--------------------------------------------------")
    print(f"BÀI BÁO GỐC:\n  ID: {input_id}\n  Tiêu đề: {id_to_title.get(input_id, 'Không rõ tiêu đề')}")
    print("--------------------------------------------------")
    
    # Lấy khuyến nghị
    recommendations = get_recommendations(input_id, num_recommendations=5)
    
    if recommendations:
        print(f"CÁC BÀI BÁO TƯƠNG TỰ ĐƯỢC KHUYẾN NGHỊ:")
        for i, rec_id in enumerate(recommendations):
            print(f" {i+1}. ID: {rec_id}\n    Tiêu đề: {id_to_title.get(rec_id, 'Không rõ tiêu đề')}\n")