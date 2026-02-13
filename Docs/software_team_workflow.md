# Hướng dẫn: Mô hình Team Phát triển Phần mềm với Gemini Subagents

Tài liệu này hướng dẫn cách thiết lập một Demo mô phỏng một đội ngũ phát triển phần mềm sử dụng các Gemini Subagents chuyên biệt.

## 1. Các Vai trò trong Team (Subagents Roles)

Để mô phỏng một quy trình chuyên nghiệp, chúng ta chia Subagents thành các vai trò sau:

| Vai trò | Nhiệm vụ chính | Công cụ thường dùng |
| :--- | :--- | :--- |
| **Product Manager (PM)** | Phân tích yêu cầu, viết PRD, lập kế hoạch task. | `task.md`, `implementation_plan.md` |
| **Software Architect** | Thiết kế cấu trúc hệ thống, chọn công nghệ, thiết kế DB. | `view_file_outline`, `mermaid diagrams` |
| **Developer (Dev)** | Viết code, fix bug, thực hiện refactoring. | `run_command`, `replace_file_content` |
| **QA/Tester** | Viết test case, chạy thử nghiệm, kiểm tra lỗi. | `run_command` (npm test, pytest) |

## 2. Quy trình làm việc (Workflow)

Một chu kỳ làm việc tiêu chuẩn sẽ diễn ra như sau:

1.  **Giai đoạn Lập kế hoạch (PM/Architect)**:
    - PM nhận yêu cầu từ người dùng và phân tích.
    - Designer/Architect thiết kế cấu trúc và tạo `implementation_plan.md`.
2.  **Giai đoạn Thực thi (Developer)**:
    - Developer đọc kế hoạch và bắt đầu viết code.
    - Sử dụng các công cụ chỉnh sửa file và chạy lệnh terminal.
3.  **Giai đoạn Kiểm thử (QA)**:
    - QA chạy các lệnh test để đảm bảo code hoạt động đúng.
    - Nếu có lỗi, QA báo lại cho Developer để sửa.
4.  **Giai đoạn Hoàn thiện (PM)**:
    - Viết `walkthrough.md` để tổng kết các thay đổi.
    - Commit và Push code lên GitHub.

## 3. Cách thực hiện Demo

Để Demo hiệu quả, bạn có thể yêu cầu tôi thực hiện một tác vụ cụ thể (ví dụ: "Xây dựng tính năng Login") và quan sát cách tôi chuyển đổi giữa các chế độ:
- Chuyển sang **PLANNING** khi đóng vai PM/Architect.
- Chuyển sang **EXECUTION** khi đóng vai Developer.
- Chuyển sang **VERIFICATION** khi đóng vai QA.

---
*Tài liệu hướng dẫn bởi Gemini Subagent*
### 6. Quy tắc Quality Gate (Mới)
Để đảm bảo tính chuyên nghiệp, team tuân thủ quy tắc:
- **QA là người giữ cổng**: Nếu unit test không đạt 100%, QA không cho phép release và gửi thông tin về cho PM.
- **PM là người điều phối**: Khi nhận lỗi từ QA, PM sẽ phân tích xem lỗi nằm ở thiết kế (mời Architect) hay ở code (mời Developer) để sửa đổi.
- **Chỉ release khi QA xác nhận PASSED.**
