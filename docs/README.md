Zodiac Project

```
Zodiac là một website cung cấp thông tin về 12 con giáp, dự đoán vận mệnh, 
và phong thủy, lấy cảm hứng từ văn hóa Á Đông. 

Dự án được xây dựng bằng Django, với giao diện sang trọng, huyền bí, 
sử dụng tông màu vàng kim và đen, phù hợp với chủ đề năm Rắn Vàng 2025. 

Website hỗ trợ responsive trên cả desktop và mobile, 
mang lại trải nghiệm người dùng mượt mà.
```

Mục tiêu
```
Cung cấp thông tin chi tiết về 12 con giáp (tính cách, tương hợp, vận mệnh).
Dự đoán vận mệnh cá nhân hóa dựa trên năm sinh và giới tính.
Tạo nền tảng mở rộng cho các tính năng thương mại (cửa hàng phong thủy), cộng đồng, và blog trong tương lai.
```


1. Cấu trúc dự án

```
docs/
  ABOUT_PROJECT.md           # Thông tin chi tiết về dự án
  README.md                  # Hướng dẫn tổng quan
zodiac_project/
  home/                      # App quản lý Trang chủ và các page tĩnh
    admin.py
    apps.py
    models.py
    tests.py
    urls.py
    views.py
  manage.py                  # File quản lý Django
  static/
    assets/
      css/
        main.css             # CSS chính
        main.css.map         # Source map cho main.css
        styles-snake.css     # CSS tùy chỉnh cho chủ đề Rắn Vàng
    site_static/             # Thư mục static khác (có thể dùng cho production)
  templates/
    base.html                # Template cơ bản
  zodiac/                    # App quản lý 12 Con Giáp và Dự đoán
    admin.py
    apps.py
    models.py
    tests.py
    urls.py
    views.py
  zodiac_project/
    asgi.py
    settings.py             # Cấu hình dự án
    templates/
      home/
        index-1.html        # Template Trang chủ
      zodiac/
        fortune_telling.html # Template Dự đoán
        zodiac_signs.html   # Template 12 Con Giáp
    urls.py
    wsgi.py

```


Mô tả các app
```
home: Quản lý các page tĩnh (Trang chủ, Về chúng tôi, Liên hệ) và logic tổng quan.
zodiac: Quản lý các tính năng liên quan đến 12 con giáp (thông tin chi tiết, dự đoán vận mệnh).
```

Yêu cầu cài đặt
```
Python: 3.11
Django: 4.2 trở lên
Hệ điều hành: Windows, macOS, hoặc Linux
Trình duyệt: Chrome, Firefox, Safari (khuyến nghị phiên bản mới nhất)
```

Hướng dẫn cài đặt và chạy dự án

1.Clone repository:
```
git clone <repository-url>
cd zodiac_project
```
2.Tạo môi trường ảo (virtual environment):
```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3.Cài đặt các thư viện cần thiết:
```
pip install -r requirements.txt
```
4.Chạy migrations:
```
python manage.py makemigrations
python manage.py migrate
```
5.Chạy server:
```
python manage.py runserver
```


Tính năng hiện tại
```
Trang chủ (Home): Form tính con giáp nhanh, giới thiệu ngắn gọn.
12 Con Giáp (Zodiac Signs): Thông tin chi tiết về từng con giáp (tính cách, tương hợp, vận mệnh 2025).
Dự đoán (Fortune Telling): Dự đoán vận mệnh dựa trên năm sinh và giới tính.
Responsive: Tối ưu giao diện cho cả desktop và mobile.
```

Kế hoạch mở rộng trong tương lai

Dự án được thiết kế để dễ dàng mở rộng với các tính năng mới:


1.Thêm các app mới:
```
shop: Quản lý cửa hàng bán vật phẩm phong thủy (vòng tay, tượng con giáp).
Thư mục: zodiac_project/shop/
Tính năng: Danh sách sản phẩm, giỏ hàng, thanh toán trực tuyến.

community: Xây dựng diễn đàn hoặc khu vực thảo luận cho người dùng.
Thư mục: zodiac_project/community/
Tính năng: Bình luận, bài đăng từ người dùng, hỏi đáp.

blog: Quản lý bài viết về phong thủy, tử vi, và văn hóa 12 con giáp.
Thư mục: zodiac_project/blog/
Tính năng: Danh sách bài viết, tìm kiếm, phân loại.
```

2.Tích hợp công nghệ:
```
Chatbot AI để trả lời nhanh các câu hỏi phong thủy.
API phong thủy để tự động hóa dự đoán.
Hỗ trợ đa ngôn ngữ (tiếng Anh, tiếng Trung) để mở rộng thị trường.
```

3.Cải thiện hiện tại:
```
Thêm dữ liệu vào database (thay vì dữ liệu tĩnh trong views.py).
Tối ưu SEO với nội dung phong phú hơn (blog, bài viết chi tiết).
Thêm tính năng cá nhân hóa (dự đoán theo ngày/tháng sinh, giờ sinh).
```

Đóng góp
```
Chúng tôi hoan nghênh mọi đóng góp để cải thiện dự án. Để đóng góp:

Fork repository.
Tạo branch mới: git checkout -b feature/your-feature-name.
Commit thay đổi: git commit -m "Thêm tính năng XYZ".
Push branch: git push origin feature/your-feature-name.
Tạo Pull Request.
```

Giấy phép
```
Dự án được phát hành dưới MIT License.
```

Liên hệ
```
Nếu bạn có câu hỏi hoặc cần hỗ trợ, vui lòng liên hệ:

Email: ntdung2508@gmail.com


```