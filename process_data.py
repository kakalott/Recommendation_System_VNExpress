import os
import csv

# Thư mục gốc chứa các thể loại đã cào
ROOT_DATA_DIR = "data/results" 

# Tên tệp CSV đầu ra
OUTPUT_CSV = "articles.csv" 

print(f"Bắt đầu xử lý dữ liệu từ thư mục: {ROOT_DATA_DIR}")

# Mở tệp CSV để ghi
with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f_out:
    # Tạo đối tượng ghi CSV
    writer = csv.writer(f_out)
    
    # Ghi hàng tiêu đề (header)
    writer.writerow(["article_id", "category", "title", "full_text"])
    
    # Biến đếm số bài báo đã xử lý
    article_count = 0
    
    # Duyệt qua tất cả các thư mục và tệp tin
    for dirpath, dirnames, filenames in os.walk(ROOT_DATA_DIR):
        
        if dirpath == ROOT_DATA_DIR:
            continue
            
        category = os.path.basename(dirpath)
        print(f"Đang xử lý thể loại: {category}...")
        
        for filename in filenames:
            if filename.endswith(".txt"):
                article_id = f"{category}_{filename.replace('.txt', '')}"
                file_path = os.path.join(dirpath, filename)
                
                # =============================================================
                # KHỐI CODE ĐÃ SỬA LỖI (CẢ LỖI LOGIC VÀ LỖI INDENT)
                try:
                    # Mở tệp .txt để đọc
                    with open(file_path, "r", encoding="utf-8") as f_in:
                        # Đọc tất cả các dòng vào 1 list
                        all_lines = f_in.readlines()
                    
                    # BƯỚC QUAN TRỌNG: Làm sạch và lọc bỏ các dòng trống
                    cleaned_lines = [line.strip() for line in all_lines if line.strip()]

                    # Kiểm tra xem file này có nội dung hay không (sau khi đã lọc)
                    if cleaned_lines:
                        # Dòng CÓ CHỮ đầu tiên (vị trí [0]) là TIÊU ĐỀ
                        title = cleaned_lines[0]
                        
                        # TẤT CẢ các dòng CÓ CHỮ còn lại (từ [1:]) là NỘI DUNG
                        full_text = " ".join(cleaned_lines[1:])
                        
                        # Ghi vào tệp CSV
                        writer.writerow([article_id, category, title, full_text])
                        article_count += 1
                    
                    else:
                        # Bỏ qua nếu file này hoàn toàn trống
                        print(f"CẢNH BÁO: Tệp {file_path} bị rỗng hoặc chỉ chứa dòng trống, bỏ qua.")

                except Exception as e:
                    print(f"Lỗi khi đọc tệp {file_path}: {e}")
                # =============================================================

print(f"\nHoàn tất! Đã xử lý và hợp nhất {article_count} bài báo vào tệp {OUTPUT_CSV}.")