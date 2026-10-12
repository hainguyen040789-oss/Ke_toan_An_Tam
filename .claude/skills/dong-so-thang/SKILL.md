---
name: dong-so-thang
description: Quy trình khóa sổ kế toán cuối tháng cho công ty sản xuất bánh, gồm đối chiếu tiền, kho, công nợ, tính lương, phân bổ, tính giá thành, kết chuyển và lập báo cáo. Dùng khi kế toán trưởng yêu cầu "khóa sổ", "đóng sổ tháng", "chốt số liệu tháng".
---

# Khóa sổ cuối tháng

Kỳ cần khóa sổ do người dùng chỉ định (YYYY-MM). Tạo file `bao-cao/<YYYY-MM>/checklist-khoa-so.md` chép danh sách dưới đây, rồi đánh dấu `[x]`, ghi kết quả và chênh lệch cho từng bước. Bước nào không làm được vì thiếu dữ liệu thì ghi rõ còn thiếu dữ liệu gì và ai cần cung cấp.

## Bước 1: Tiền
- [ ] Đối chiếu sổ quỹ tiền mặt với biên bản kiểm quỹ cuối tháng.
- [ ] Đối chiếu sổ phụ / sao kê từng tài khoản ngân hàng với TK 112.
- [ ] Liệt kê các khoản tiền về chưa xác định khách hàng.

## Bước 2: Hóa đơn
- [ ] Đối chiếu hóa đơn đầu ra trên hệ thống hóa đơn điện tử với doanh thu TK 511 và thuế 33311.
- [ ] Đối chiếu hóa đơn đầu vào (tải từ cổng của cơ quan thuế) với sổ: tìm hóa đơn chưa hạch toán, hóa đơn sai thông tin, nhà cung cấp có rủi ro.

## Bước 3: Kho (dùng skill `kiem-ke-kho` nếu có kiểm kê)
- [ ] Tồn đầu + nhập − xuất = tồn cuối cho 152, 153, 155, 157 theo từng mã hàng.
- [ ] Không có mã hàng tồn âm.
- [ ] Danh sách thành phẩm cận date / hết hạn, kèm đề xuất xử lý.
- [ ] Đối chiếu hàng gửi đại lý / siêu thị (157) với xác nhận của bên nhận.

## Bước 4: Công nợ
- [ ] Bảng tuổi nợ phải thu (131); nợ quá hạn trên 90 ngày cần đề xuất dự phòng.
- [ ] Đối chiếu phải trả nhà cung cấp chính (331).
- [ ] Tính chiết khấu theo doanh số / hỗ trợ bán hàng phát sinh trong tháng theo hợp đồng.

## Bước 5: Lương và bảo hiểm
- [ ] Bảng lương từ bảng chấm công (ca, làm thêm giờ, phụ cấp ca đêm).
- [ ] Trích BHXH/BHYT/BHTN/KPCĐ theo tỷ lệ trong `kien-thuc/thue-va-phap-ly.md`.
- [ ] Khấu trừ thuế TNCN.
- [ ] Phân loại chi phí lương: 622 (công nhân trực tiếp) / 6271 / 641 / 642.

## Bước 6: Phân bổ và trích trước
- [ ] Khấu hao TSCĐ (lò nướng, máy trộn, dây chuyền đóng gói, xe lạnh).
- [ ] Phân bổ chi phí trả trước (242), công cụ dụng cụ.
- [ ] Trích trước chi phí điện, nước, gas nếu chưa có hóa đơn.

## Bước 7: Giá thành
- [ ] Chạy skill `tinh-gia-thanh` cho kỳ này.
- [ ] Giải trình các chênh lệch NVL vượt ngưỡng so với định mức.
- [ ] Hạch toán nhập kho thành phẩm và giá vốn hàng bán.

## Bước 8: Thuế
- [ ] Bù trừ thuế GTGT đầu vào / đầu ra, xác định số phải nộp hoặc còn được khấu trừ.
- [ ] Nếu là tháng cuối quý: ước tính số tạm nộp TNDN.

## Bước 9: Kết chuyển và báo cáo
- [ ] Kết chuyển doanh thu, giảm trừ, giá vốn, chi phí sang TK 911; xác định lãi/lỗ.
- [ ] Bảng cân đối số phát sinh: tổng Nợ = tổng Có; các tài khoản lưỡng tính trình bày đúng.
- [ ] Báo cáo quản trị nhanh: doanh thu và lãi gộp theo dòng bánh và theo kênh; so sánh với tháng trước và kế hoạch.

## Đầu ra
1. `bao-cao/<YYYY-MM>/checklist-khoa-so.md` (đầy đủ trạng thái các bước)
2. `bao-cao/<YYYY-MM>/but-toan-cuoi-ky.md` (bút toán đề xuất)
3. `bao-cao/<YYYY-MM>/bao-cao-quan-tri.md`
4. Tóm tắt cho kế toán trưởng: kết quả lãi/lỗ, 3–5 vấn đề lớn nhất, các việc cần quyết định.
