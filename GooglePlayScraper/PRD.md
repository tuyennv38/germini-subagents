# PRD: Google Play Review Crawler (Cron Job)

## 1. Mục tiêu
Xây dựng một ứng dụng chạy định kỳ (cron) để tự động thu thập (crawl) các bình luận đánh giá (reviews) của người dùng từ một ứng dụng cụ thể trên Google Play Store và lưu trữ vào cơ sở dữ liệu SQLite.

## 2. Tính năng chính (MVP)
- **Cấu hình**: Cho phép nhập ID ứng dụng (Package Name) trực tiếp từ bàn phím khi chạy.
- **Thu thập dữ liệu**: Lấy thông tin: Tên người dùng, Số sao (Rating), Nội dung bình luận (Review), Thời gian.
- **Lưu trữ**: Lưu dữ liệu vào file SQLite để quản lý lâu dài, tránh trùng lặp dữ liệu.
- **Hiển thị**: Sau khi cào, hiển thị ngay Top 5 bình luận mới nhất lên màn hình.
- **Chế độ Cron**: Hỗ trợ chạy định kỳ (mô phỏng hoặc thực tế).

## 3. Yêu cầu kỹ thuật
- **Ngôn ngữ**: Python.
- **Thư viện**: `google-play-scraper` (thư viện phổ biến cho Python).
- **Database**: SQLite3.

---
*Created by product_manager subagent*
