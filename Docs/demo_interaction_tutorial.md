# Hướng dẫn Demo: Quy trình làm việc của Team Subagents

Chào mừng bạn đến với mô phỏng quy trình làm việc thực tế. Dưới đây là cách bạn có thể yêu cầu "Đội ngũ AI" này làm việc cho bạn trong Gemini-CLI.

## 1. Chuẩn bị
Hãy đảm bảo bạn đã:
1. Copy các file trong `.gemini/agents/` vào thư mục dự án của bạn (nếu dùng toàn cục).
2. Sửa `settings.json` của Gemini-CLI: `"enableAgents": true`.
3. Trong CLI, gõ lệnh: `/agents refresh`

## 2. Kịch bản Demo: Yêu cầu tính năng mới
Thay vì yêu cầu chung chung, hãy thử đưa ra một yêu cầu mang tính "khởi đầu dự án" để **product_manager** vào cuộc.

**Ví dụ yêu cầu (Copy & Paste vào Gemini-CLI):**
> "Tôi muốn xây dựng một ứng dụng ghi chú đơn giản bằng Python. Team hãy bắt đầu làm việc: product_manager hãy phân tích yêu cầu và viết PRD, sau đó architect hãy thiết kế cấu trúc, rồi developer hãy viết code cơ bản."

## 3. Cách hệ thống tự động điều phối
Khi bạn gửi yêu cầu trên, đây là điều sẽ xảy ra "dưới nắp máy":

1. **Agent chính (Orchestrator)**: Đọc yêu cầu của bạn -> Quét danh sách agents -> Thấy `product_manager` có mô tả là "phân tích yêu cầu và viết PRD".
2. **Kích hoạt PM**: Agent chính sẽ gọi công cụ `product_manager(task="...")`.
3. **PM làm việc**: Agent PM sẽ đọc yêu cầu, tạo file `PRD.md` và cập nhật `task.md`.
4. **Bàn giao (Handover)**: PM kết thúc nhiệm vụ -> Agent chính lại quét tiếp -> Thấy `architect` phù hợp để làm bước tiếp theo dựa trên PRD đã có.

## 4. Mẹo để Demo thành công
- **Giao việc cụ thể**: "developer hãy cài thêm thư viện Flask cho tôi" -> Agent chính sẽ biết chỉ cần gọi `developer`.
- **Kiểm tra tiến độ**: Bạn có thể hỏi: "Trạng thái dự án hiện tại thế nào?" -> Hệ thống thường sẽ gọi `product_manager` để đọc file `task.md`.
- **Yêu cầu QA**: "qa hãy chạy thử code và báo cáo lỗi nếu có" -> Agent `qa` sẽ được kích hoạt để dùng `run_command` kiểm tra.

---
*Bây giờ bạn hãy thử copy câu lệnh ví dụ ở mục 2 và dán vào Gemini-CLI của mình nhé!*
