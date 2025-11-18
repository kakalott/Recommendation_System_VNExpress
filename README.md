# VN Express article crawler
[![Python 3.10.7](https://img.shields.io/badge/python-3.10.7-blue)](https://www.python.org/downloads/release/python-3107/)[![BeautifulSoup 0.0.1](https://img.shields.io/badge/BeautifulSoup-0.0.1-purple)](https://pypi.org/project/bs4/)[![Requests 2.28.1](https://img.shields.io/badge/Requests-2.28.1-black)](https://pypi.org/project/requests/)[![tqdm 4.64.1](https://img.shields.io/badge/tqdm-4.64.1-orange)](https://pypi.org/project/tqdm/)   
Crawling titles and paragraphs of VN Express articles using their URLs or categories names 

## Installation
Create virtual environment then install required packages:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Usage
### Crawl by URL
To crawl by URLs, you need to provide them in a text file and then give their path inside the `--input` flag (default is `urls.txt`)  
```bash
python urls_crawler.py [-h] [--input URLS_FPATH] [--output OUTPUT_DPATH]

options:
  -h, --help            show this help message and exit
  --input URLS_FPATH    urls txt file path
  --output OUTPUT_DPATH saved directory path
```

### Crawl by category name
You can crawl a number of articles by one type or all types based on the flags you use. Currently, my program only supports the following categories:
```bash
thoi-su
du-lich
the-gioi
kinh-doanh
khoa-hoc
giai-tri
the-thao
phap-luat
giao-duc
suc-khoe
doi-song
```  
To crawl article in a single type, you must provide type name in `--type` flag and number of pages you want to crawl in `--pages` flag.  
For example if you run below command:  
```bash
python types_crawler.py --type khoa-hoc --pages 3
```  
It will crawl articles from
```
https://vnexpress.net/khoa-hoc-p1
https://vnexpress.net/khoa-hoc-p2
https://vnexpress.net/khoa-hoc-p3
```  
To crawl article in all categories, you need to provide `--all` flag and number of pages `--pages` instead.  
```bash
python types_crawler.py [-h] [--type ARTICLE_TYPE] [--all] [--pages TOTAL_PAGES] [--output OUTPUT_DPATH]

optional arguments:
  -h, --help            show this help message and exit
  --type ARTICLE_TYPE   name of articles type
  --all                 crawl all of types
  --pages TOTAL_PAGES   number of pages to crawl per type
  --output OUTPUT_DPATH
                        saved directory path
```

## Appendix
I've crawled all categories of articles with 20 pages each that you can download [here](https://drive.google.com/file/d/1zgS3nldOGW90QKgumNtbarScqtycTLsz/view?usp=sharing).
## Todo
- [ ] Add logging module
- [ ] Crawl in other news websites

**Hệ thống Khuyến nghị Bài báo VNExpress (Lọc dựa trên Nội dung)**

Dự án này là một hệ thống khuyến nghị bài báo đơn giản, được xây dựng dựa trên dữ liệu cào từ trang vnexpress.net.

Hệ thống này triển khai phương pháp Lọc dựa trên Nội dung (Content-Based Filtering). Logic hoạt động cốt lõi là: Nếu người dùng đọc một bài báo, hệ thống sẽ gợi ý các bài báo khác có nội dung tương tự nhất.

📜 **Cơ sở Lý thuyết**
Dự án này được xây dựng dựa trên lý thuyết tại Mục 6.2 (Lọc dựa trên nội dung) của giáo trình "Nhập môn Khoa học Dữ liệu".

Hồ sơ Sản phẩm (Item Profiles): Chúng ta định nghĩa "hồ sơ" của mỗi bài báo chính là toàn bộ nội dung văn bản (tiêu đề + mô tả + các đoạn văn) của bài báo đó.

Vector Đặc trưng (Feature Vector): Để máy tính hiểu được văn bản, chúng ta sử dụng kỹ thuật TF-IDF (TfidfVectorizer) để chuyển đổi mỗi "hồ sơ" văn bản thành một vector số.

Độ tương đồng (Similarity): Chúng ta sử dụng phép toán Độ tương đồng Cosine (Cosine Similarity) để tính toán một ma trận, cho biết mức độ giống nhau (từ 0 đến 1) giữa mọi cặp bài báo.

Khuyến nghị: Khi người dùng đọc một bài báo, hệ thống sẽ tra cứu ma trận này và trả về 5 bài báo có điểm tương đồng cao nhất.

🗂️ **Cấu trúc Dự án**
.
├── venv/                   # Môi trường ảo Python
├── data/                   # Thư mục chứa dữ liệu cào thô (dạng .txt)
│   ├── results/
│   │   ├── thoi-su/
│   │   ├── du-lich/
│   │   └── ...
│   └── urls/
├── articles.csv            # Dữ liệu đã hợp nhất và làm sạch
├── tfidf_model.pkl         # Mô hình TF-IDF đã được huấn luyện
├── similarity_model.npz    # Ma trận tương đồng (Cosine Similarity)
│
├── urls_crawler.py         # Script cào theo danh sách URL
├── types_crawler.py        # Script cào theo Thể loại (CHẠY BƯỚC 1)
├── utils.py                # Các hàm hỗ trợ cào
│
├── process_data.py         # Script xử lý dữ liệu (CHẠY BƯỚC 2)
├── build_model.py          # Script xây dựng model TF-IDF (CHẠY BƯỚC 3)
├── build_similarity.py     # Script tính toán ma trận tương đồng (CHẠY BƯỚC 4)
├── recommend.py            # Script chạy khuyến nghị (CHẠY BƯỚC 5)
│
├── requirements.txt        # Các thư viện Python gốc
└── README.md               # Tệp hướng dẫn này
⚙️ **Cài đặt**
Clone repository này về máy.

Mở terminal, di chuyển vào thư mục VNExpressCrawler.

Tạo và kích hoạt môi trường ảo:

Bash

python -m venv venv
venv\Scripts\activate
Cài đặt các thư viện cần thiết:

Bash

# Cài các thư viện gốc
pip install -r requirements.txt

# Cài các thư viện cho mô hình khuyến nghị
pip install pandas scikit-learn
🚀 **Hướng dẫn sử dụng (Toàn bộ quy trình)**
Để chạy hệ thống từ đầu đến cuối, bạn cần thực hiện 5 bước sau theo thứ tự:

**Bước 1**: Cào Dữ liệu
Chạy script types_crawler.py để cào dữ liệu từ VNExpress.

--all: Cào tất cả 11 thể loại.

--pages 10: Cào 10 trang đầu tiên của mỗi thể loại.

--output data: Lưu kết quả vào thư mục data.

Bash

python types_crawler.py --all --pages 10 --output data
Kết quả: Thư mục data/results/ chứa đầy các tệp .txt.

**Bước 2**: Hợp nhất Dữ liệu
Chạy script process_data.py để gom tất cả các tệp .txt vào một tệp articles.csv duy nhất.

Bash

python process_data.py
Kết quả: Một tệp articles.csv được tạo ra.

**Bước 3**: Xây dựng Model TF-IDF
Chạy script build_model.py để đọc tệp .csv và tạo ma trận TF-IDF.

Bash

python build_model.py
Kết quả: Một tệp tfidf_model.pkl được tạo ra, chứa các vector đặc trưng của bài báo.

**Bước 4**: Xây dựng Model Tương đồng
Chạy script build_similarity.py để tính toán độ tương đồng cosine giữa tất cả các bài báo.

Bash

python build_similarity.py
Kết quả: Một tệp similarity_model.npz được tạo ra, chứa "bộ não" của hệ khuyến nghị.

**Bước 5**: Nhận Khuyến nghị
Chạy script recommend.py để xem kết quả.

Cách 1: Chạy với ID mẫu (mặc định)

Bash

python recommend.py
Cách 2: Chạy với ID bài báo cụ thể (Bạn có thể tìm ID trong tệp articles.csv, ví dụ: giai-tri_url_001)

Bash

python recommend.py giai-tri_url_001
💡**** Ví dụ Kết quả****
Chạy lệnh python recommend.py thoi-su_url_316:

--------------------------------------------------
BÀI BÁO GỐC:
  ID: thoi-su_url_316
  Tiêu đề: [Tiêu đề của bài báo 316]
--------------------------------------------------
CÁC BÀI BÁO TƯƠNG TỰ ĐƯỢC KHUYẾN NGHỊ:
 1. ID: thoi-su_url_120
    Tiêu đề: [Tiêu đề của bài báo 120]

 2. ID: thoi-su_url_045
    Tiêu đề: [Tiêu đề của bài báo 045]

 3. ID: thoi-su_url_211
    Tiêu đề: [Tiêu đề của bài báo 211]

 4. ID: thoi-su_url_009
    Tiêu đề: [Tiêu đề của bài báo 009]

 5. ID: thoi-su_url_158
    Tiêu đề: [Tiêu đề của bài báo 158]