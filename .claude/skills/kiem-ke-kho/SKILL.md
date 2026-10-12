---
name: kiem-ke-kho
description: Đối chiếu nhập – xuất – tồn và kiểm kê kho nguyên liệu, bao bì, thành phẩm bánh; xử lý chênh lệch, hàng cận date, hết hạn. Dùng khi kế toán trưởng yêu cầu kiểm kê, đối chiếu kho, rà soát hàng cận date hoặc lập dự phòng tồn kho.
---

# Kiểm kê và kiểm soát kho

## Đầu vào
- Sổ chi tiết vật tư / thành phẩm từ phần mềm (mã, tên, số lô, hạn sử dụng, số lượng, giá trị).
- Biên bản kiểm kê thực tế (số lượng đếm được theo mã và theo lô).

## Các bước
1. **Kiểm tra cân đối:** tồn đầu + nhập − xuất = tồn cuối theo từng mã. Liệt kê mã bị tồn âm hoặc có đơn giá bất thường (lệch quá 20% so với giá mua gần nhất).
2. **Chênh lệch kiểm kê:** sổ sách so với thực tế, theo mã và theo lô.
   - Thiếu trong định mức hao hụt (bột, đường rơi vãi, độ ẩm): Nợ 632 / Có 152, 155.
   - Thiếu ngoài định mức: Nợ 1381 chờ xử lý, đề xuất xác định trách nhiệm (Nợ 1388 / Nợ 334 / Nợ 632).
   - Thừa: Nợ 152, 155 / Có 3381 chờ xử lý.
3. **Hạn sử dụng (FEFO):** phân nhóm thành phẩm và NVL dễ hỏng (bơ, trứng, sữa, nhân) theo số ngày còn lại:
   - Đã hết hạn: đề xuất tiêu hủy; chuẩn bị danh mục hồ sơ (quyết định lập hội đồng, biên bản, bảng kê lô, hình ảnh).
   - Còn dưới 30% hạn sử dụng: đề xuất đẩy bán hoặc khuyến mại; xem xét trích dự phòng 2294 theo giá trị thuần có thể thực hiện được.
4. **Bao bì lỗi thời:** hộp, nhãn của mùa trước hoặc mẫu cũ không còn dùng được, đề xuất xử lý.
5. **Hàng gửi bán (157):** đối chiếu với biên bản xác nhận tồn của đại lý / siêu thị.

## Đầu ra
`bao-cao/<YYYY-MM>/kiem-ke-kho.md`, gồm: bảng chênh lệch, danh sách cận date / hết hạn kèm giá trị, bút toán đề xuất, hồ sơ cần bổ sung.
