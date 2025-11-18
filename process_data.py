import os
import csv

# Thư mục gốc chứa các thể loại đã cào (dựa trên code của bạn)
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
    # os.walk sẽ đi vào từng thư mục con
    for dirpath, dirnames, filenames in os.walk(ROOT_DATA_DIR):
        
        # Bỏ qua thư mục gốc, chỉ xử lý các thư mục con (như 'thoi-su', 'du-lich')
        if dirpath == ROOT_DATA_DIR:
            continue
            
        # Lấy tên thể loại từ tên thư mục
        category = os.path.basename(dirpath)
        print(f"Đang xử lý thể loại: {category}...")
        
        for filename in filenames:
            # Chỉ xử lý các tệp .txt
            if filename.endswith(".txt"):
                # Tạo một ID bài báo duy nhất (ví dụ: thoi-su_url_001)
                article_id = f"{category}_{filename.replace('.txt', '')}"
                
                # Đường dẫn đầy đủ đến tệp .txt
                file_path = os.path.join(dirpath, filename)
                
                try:
                    # Mở tệp .txt để đọc
                    with open(file_path, "r", encoding="utf-8") as f_in:
                        # Đọc tất cả các dòng
                        lines = f_in.readlines()
                        
                        # Dựa trên file utils.py, dòng đầu tiên là TIÊU ĐỀ
                        title = lines[0].strip()
                        
                        # Các dòng còn lại là NỘI DUNG
                        # Dùng list comprehension để làm sạch và nối các dòng
                        content_lines = [line.strip() for line in lines[1:] if line.strip()]
                        full_text = " ".join(content_lines)
                        
                        # Ghi vào tệp CSV
                        writer.writerow([article_id, category, title, full_text])
                        article_count += 1
                        
                except Exception as e:
                    print(f"Lỗi khi đọc tệp {file_path}: {e}")

print(f"\nHoàn tất! Đã xử lý và hợp nhất {article_count} bài báo vào tệp {OUTPUT_CSV}.")