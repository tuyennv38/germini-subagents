# Technical Design: Google Play Review Crawler

## 1. Database Schema (SQLite)
Bảng `reviews`:
- `reviewId`: PRIMARY KEY (Dùng ID từ Google Play để tránh trùng).
- `userName`: TEXT.
- `content`: TEXT.
- `score`: INTEGER.
- `at`: DATETIME.
- `appVersion`: TEXT.

## 2. Quy trình Crawler
1. **Khởi tạo**: Kết nối SQLite, tạo bảng nếu chưa có.
2. **Fetch**: Sử dụng thư viện `google-play-scraper` lấy N review mới nhất.
3. **Upsert**: Lưu dữ liệu vào SQLite. Dùng câu lệnh `INSERT OR IGNORE` để chỉ lưu những review chưa tồn tại dựa trên `reviewId`.
4. **Log**: Ghi lại số lượng review mới đã được thêm.

## 3. Automation (Cron)
- Sử dụng thư viện `schedule` trong Python hoặc hướng dẫn người dùng thiết lập Windows Task Scheduler.
- File đầu vào chính: `scraper.py`.

---
*Created by architect subagent*
