# Phòng kế toán – Công ty sản xuất bánh

Repository này chứa agent hỗ trợ vận hành phòng kế toán. Người dùng chính là **kế toán trưởng**.

- Agent chính: `.claude/agents/ke-toan-van-hanh.md`. Với mọi yêu cầu nghiệp vụ kế toán, giao cho agent này.
- Skill quy trình: `dong-so-thang`, `tinh-gia-thanh`, `ke-khai-thue`, `kiem-ke-kho` (trong `.claude/skills/`).
- Kiến thức nền: `kien-thuc/` (hồ sơ công ty, nghiệp vụ ngành bánh, thuế).
- Dữ liệu đầu vào: `du-lieu/<YYYY-MM>/` (không sửa dữ liệu gốc). Kết quả: `bao-cao/<YYYY-MM>/`.
- Công cụ: `cong-cu/tinh_gia_thanh.py` (Python 3, chỉ dùng thư viện chuẩn).
- Luôn trả lời bằng tiếng Việt. Mọi kết quả là bản đề xuất chờ kế toán trưởng duyệt.

## Học tập của các con

- Agent giáo viên: `.claude/agents/giao-vien-gia-dinh.md` – dạy Toán, Tiếng Anh, Tự nhiên – Xã hội cho 3 bé lớp 2, 6, 9. Mọi yêu cầu học tập giao cho agent này.
- Hồ sơ học sinh: `hoc-tap/ho-so-hoc-sinh.md`. Lịch học: `hoc-tap/lich-hoc.md`. Bài luyện: `hoc-tap/bai-lam/`. Nhật ký: `hoc-tap/nhat-ky/`.
