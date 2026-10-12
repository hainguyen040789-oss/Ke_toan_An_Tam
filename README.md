# Kế toán An Tâm: agent vận hành phòng kế toán công ty sản xuất bánh

Agent chạy trong **Claude Code** để hỗ trợ kế toán trưởng: hạch toán, tính giá thành bánh, kiểm kê kho, công nợ, lương và bảo hiểm, kê khai thuế, khóa sổ và báo cáo.

## Bắt đầu
1. Điền thông tin vào `kien-thuc/ho-so-cong-ty.md` (chế độ kế toán, kỳ kê khai, danh mục bánh, phương pháp tính giá…).
2. Mở repo này bằng Claude Code (claude.ai/code hoặc chạy lệnh `claude` trong thư mục).
3. Giao việc bằng tiếng Việt, ví dụ:
   - "Dùng agent ke-toan-van-hanh khóa sổ tháng 10/2026, dữ liệu ở du-lieu/2026-10"
   - "Tính giá thành tháng này, giải trình vì sao bơ vượt định mức"
   - "Hàng bánh trung thu đại lý trả về sau mùa thì hạch toán thế nào?"
   - "Còn bao nhiêu ngày đến hạn nộp tờ khai GTGT quý 3? Chuẩn bị bảng đối chiếu"

## Cấu trúc
| Thư mục | Nội dung |
|---|---|
| `.claude/agents/ke-toan-van-hanh.md` | Định nghĩa agent: vai trò, phạm vi, nguyên tắc |
| `.claude/skills/` | Quy trình: `dong-so-thang`, `tinh-gia-thanh`, `ke-khai-thue`, `kiem-ke-kho` |
| `kien-thuc/` | Hồ sơ công ty, nghiệp vụ đặc thù ngành bánh, thuế và pháp lý |
| `cong-cu/tinh_gia_thanh.py` | Tính giá thành theo định mức và hệ số, phân tích chênh lệch NVL |
| `du-lieu/mau/` | Dữ liệu mẫu, xem định dạng CSV đầu vào |
| `bao-cao/` | Nơi agent ghi kết quả |

Chạy thử với dữ liệu mẫu:
```bash
python3 cong-cu/tinh_gia_thanh.py du-lieu/mau --nguong 3
```

## Lưu ý
- Mọi kết quả là **bản đề xuất**; kế toán trưởng kiểm tra và chịu trách nhiệm phê duyệt.
- Quy định thuế thay đổi thường xuyên. Các điểm đánh dấu **[CẦN KIỂM TRA]** phải được đối chiếu với văn bản hiện hành; cập nhật `kien-thuc/thue-va-phap-ly.md` khi có văn bản mới.
- Không đưa dữ liệu lương hoặc thông tin cá nhân lên repo công khai. Repo hiện đang **public**: nên chuyển sang **private** trước khi đưa dữ liệu thật vào.
