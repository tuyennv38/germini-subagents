# Technical Design: Calculator Web App

## 1. Kiến trúc Giao diện (UI)
- Sử dụng **Flexbox** để căn giữa các phần tử.
- Bảng điều khiển gồm:
  - 2 Input trường số (Number input).
  - Khối phím chức năng (+, -, *, /) xếp hàng ngang.
  - Khu vực hiển thị kết quả nổi bật.

## 2. Xử lý Logic (JavaScript)
- Tách biệt logic tính toán (Model) và logic điều khiển UI (Controller).
- **Hàm `calculate(num1, num2, operator)`**:
  - Đầu vào: 2 số, 1 chuỗi ký tự toán tử.
  - Xử lý: Kiểm tra số hợp lệ, thực hiện phép tính, xử lý lỗi chia cho 0.

## 3. Chiến lược Kiểm thử (QA Strategy)
- Tạo file `test.js` sử dụng Node.js (cơ bản) hoặc chạy trực tiếp trên console để verify logic.
- Phải test các case:
  - Phép chia 0: Trả về thông báo lỗi thay vì "Infinity".
  - Ký tự lạ: Ngăn chặn nhập chữ.

---
*Created by architect subagent*
