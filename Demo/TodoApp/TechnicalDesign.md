# Technical Design: Todo App

## 1. Kiến trúc
Ứng dụng sử dụng mô hình Client-Server đơn giản.

## 2. Cấu trúc thư mục
- `server.js`: Web server sử dụng Express.
- `public/`: Thư mục chứa giao diện web.
  - `index.html`: Cấu trúc trang web.
  - `style.css`: Định dạng giao diện.
  - `script.js`: Logic tương tác phía client.

## 3. API Endpoints
- `GET /api/todos`: Lấy danh sách todos.
- `GET /api/time`: (Mới) Lấy giờ hiện tại của server.
- `POST /api/todos`: Thêm todo mới (body: `{ "text": "..." }`).
- `DELETE /api/todos/:id`: Xóa todo theo ID.

## 4. Workflow thực thi
1. **Dev**: Init `package.json`, cài đặt `express`.
2. **Dev**: Viết `server.js` (Thêm endpoint `/api/time`).
3. **Dev**: Viết nội dung thư mục `public/` (Thêm đồng hồ hiển thị).
4. **QA**: Chạy server và test các API.

---
*Created by Architect Subagent*
