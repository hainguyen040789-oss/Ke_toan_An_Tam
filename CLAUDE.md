# Phòng kế toán – Công ty sản xuất bánh

Repository này chứa agent hỗ trợ vận hành phòng kế toán. Người dùng chính là **kế toán trưởng**.

- Agent chính: `.claude/agents/ke-toan-van-hanh.md`. Với mọi yêu cầu nghiệp vụ kế toán, giao cho agent này.
- Skill quy trình: `dong-so-thang`, `tinh-gia-thanh`, `ke-khai-thue`, `kiem-ke-kho` (trong `.claude/skills/`).
- Kiến thức nền: `kien-thuc/` (hồ sơ công ty, nghiệp vụ ngành bánh, thuế).
- Dữ liệu đầu vào: `du-lieu/<YYYY-MM>/` (không sửa dữ liệu gốc). Kết quả: `bao-cao/<YYYY-MM>/`.
- Công cụ: `cong-cu/tinh_gia_thanh.py` (Python 3, chỉ dùng thư viện chuẩn).
- Luôn trả lời bằng tiếng Việt. Mọi kết quả là bản đề xuất chờ kế toán trưởng duyệt.

## Học tập (ngoài kế toán)

- Agent `giao-vien-da-mon` (`.claude/agents/giao-vien-da-mon.md`): kèm học THCS lớp 6–9 đa môn cho Hải Đan. Với yêu cầu học tập, giao cho agent này. Tài liệu học lưu trong `hoc-tap/`.
