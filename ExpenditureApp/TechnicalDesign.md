# Technical Design: Expense Management App

## 1. Cấu trúc thư mục
- `ExpenditureApp/`
  - `app.py`: Điểm khởi đầu của ứng dụng.
  - `expenses.json`: Lưu trữ dữ liệu.

## 2. Cấu trúc dữ liệu (JSON)
```json
[
  {
    "id": 1,
    "description": "Ăn sáng",
    "amount": 35000,
    "date": "2026-02-13"
  }
]
```

## 3. Kế hoạch triển khai
1. Định nghĩa class `ExpenseManager` để xử lý Đọc/Ghi file JSON.
2. Xây dựng vòng lặp CLI (Menu) để người dùng chọn chức năng.

---
*Created by architect subagent*
