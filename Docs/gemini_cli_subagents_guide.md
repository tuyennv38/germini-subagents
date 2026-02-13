# Hướng dẫn tạo Subagents với Gemini-CLI

Gemini-CLI cho phép bạn mở rộng khả năng của mình thông qua các "Subagents" chuyên biệt. Đây là các bước để tạo và sử dụng chúng.

## 1. Cấu trúc thư mục
Các subagents được định nghĩa dưới dạng file Markdown trong thư mục:
- Dự án: `.gemini/agents/*.md`
- Toàn cục: `~/.gemini/agents/*.md`

## 2. Định nghĩa Subagent
Một file subagent cần có phần **YAML frontmatter** ở đầu để cấu hình:

```yaml
---
name: [Tên agent]
description: [Mô tả nhiệm vụ - dùng để agent chính biết khi nào nên gọi]
tools: [danh sách các tool agent được phép dùng]
model: inherit (hoặc gemini-pro, v.v.)
---
[Hệ thống Prompt - chỉ dẫn cho agent này]
```

## 3. Cách kích hoạt trong Demo
Để demo tính năng này, bạn cần đảm bảo Gemini-CLI đã được bật tính năng thực nghiệm trong `settings.json`:

```json
{
  "experimental": {
    "enableAgents": true
  }
}
```

## 4. Cách sử dụng
1. Sau khi tạo file `.md`, gõ `/agents refresh` trong Gemini-CLI để cập nhật.
2. Agent chính sẽ tự động gọi Subagent nếu câu hỏi của bạn khớp với `description` của subagent đó.
3. Hoặc bạn có thể gọi trực tiếp bằng Markdown (nếu CLI hỗ trợ).

---
*Tài liệu hướng dẫn bởi Gemini Subagent*
