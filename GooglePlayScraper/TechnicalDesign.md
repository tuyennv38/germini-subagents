# Technical Design: Google Play Review Crawler

## 1. Database Schema (SQLite)
Bảng `reviews`:
- `reviewId`: PRIMARY KEY.
- `appId`: TEXT (ID của từng ứng dụng để phân biệt).
- `userName`, `content`, `score`, `at`, `appVersion`.

## 2. Quy trình Crawler (Cải tiến)
1. **Khởi tạo**: Kết nối SQLite, tạo bảng.
2. **Input**: Yêu cầu người dùng nhập Package Name qua terminal.
3. **Fetch**: Lấy dữ liệu từ Google Play.
4. **Upsert**: Lưu vào database (mặc định tránh trùng).
5. **Display**: Truy vấn database để lấy 5 bản ghi mới nhất vừa cào và in ra terminal theo định dạng sạch đẹp.

## 3. Automation (Cron)
- File `scraper.py` hỗ trợ cả chạy tương tác (Manual) và chạy tham số (cho Cron nếu cần mở rộng sau này).

---
*Created by architect subagent*
