# Hướng dẫn chuyển sang dùng Claude Code trên máy tính

## 1. Cài đặt (một lần)
- **Python 3** (để chạy `cong-cu/tinh_gia_thanh.py`): tải tại python.org. Khi cài trên Windows, tick "Add Python to PATH".
- **Claude Code**, chọn một trong hai cách:
  - **Ứng dụng Claude Desktop** (Windows/Mac): tải tại claude.ai/download, đăng nhập, mở tab **Code**.
  - **Dòng lệnh:** cài theo hướng dẫn tại https://code.claude.com/docs, sau đó chạy `claude` trong thư mục dự án.

## 2. Lấy dữ liệu về máy
Chọn một trong hai cách:
- **Từ file nén:** giải nén `Ke_toan_An_Tam.zip` vào một thư mục, ví dụ `D:\Ke_toan_An_Tam` hoặc `~/Ke_toan_An_Tam`.
- **Từ GitHub (khuyến nghị, có lịch sử thay đổi):**
  ```bash
  git clone https://github.com/hainguyen040789-oss/Ke_toan_An_Tam.git
  cd Ke_toan_An_Tam
  git checkout ccr-fa4ba233-m2hozu
  ```

## 3. Mở và sử dụng
1. Mở thư mục `Ke_toan_An_Tam` bằng Claude Code (Desktop: chọn thư mục; dòng lệnh: `cd Ke_toan_An_Tam` rồi `claude`).
2. Claude tự đọc `CLAUDE.md`, agent `ke-toan-van-hanh` và các skill trong `.claude/`.
3. Kiểm tra nhanh:
   ```bash
   python3 cong-cu/tinh_gia_thanh.py du-lieu/mau --nguong 3
   ```
   (Windows có thể dùng `python` hoặc `py` thay cho `python3`.)
4. Đưa dữ liệu tháng vào `du-lieu/<YYYY-MM>/`, kết quả agent ghi vào `bao-cao/<YYYY-MM>/`.

## 4. Lưu ý bảo mật
- Repo GitHub đang **public**. Khi làm việc với dữ liệu thật (lương, hóa đơn, thông tin cá nhân) trên máy, **không đẩy lên GitHub** hoặc chuyển repo sang **private** trước.
- Sao lưu thư mục `du-lieu/` và `bao-cao/` định kỳ.

## Nội dung gói
| Thư mục/tệp | Nội dung |
|---|---|
| `CLAUDE.md` | Hướng dẫn cho Claude khi mở dự án |
| `.claude/agents/`, `.claude/skills/` | Agent kế toán và các quy trình |
| `kien-thuc/` | Hồ sơ công ty, nghiệp vụ ngành bánh, thuế; `hoi-dap/` lưu các câu đã tư vấn |
| `cong-cu/` | Công cụ tính giá thành |
| `du-lieu/mau/` | Dữ liệu mẫu |
| `bao-cao/` | Kết quả |
