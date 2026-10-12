---
name: ke-khai-thue
description: Chuẩn bị số liệu và hồ sơ kê khai thuế GTGT, TNCN, tạm nộp TNDN và quyết toán năm cho công ty sản xuất bánh; nhắc lịch nộp. Dùng khi kế toán trưởng hỏi về tờ khai thuế, hạn nộp thuế, hoặc đối chiếu hóa đơn.
---

# Chuẩn bị kê khai thuế

Agent **chỉ chuẩn bị** số liệu và bảng đối chiếu. Kế toán trưởng là người kiểm tra, ký và nộp tờ khai trên cổng thuế điện tử.

## 1. Xác định kỳ và hạn nộp
- Đọc kỳ kê khai trong `kien-thuc/ho-so-cong-ty.md` và lịch nộp trong `kien-thuc/thue-va-phap-ly.md`.
- Ghi rõ hạn nộp, và số ngày còn lại tính từ ngày hôm nay (lấy bằng lệnh `date`).

## 2. Thuế GTGT
- Bảng kê hóa đơn đầu ra theo thuế suất (0%, 5%, 8%, 10%, không chịu thuế), khớp với TK 511 và 33311.
- Bảng kê hóa đơn đầu vào đủ điều kiện khấu trừ, khớp với TK 1331. Loại ra các hóa đơn:
  - từ 5 triệu đồng trở lên mà không có chứng từ thanh toán không dùng tiền mặt [CẦN KIỂM TRA ngưỡng hiện hành];
  - của người bán ngừng hoạt động hoặc có rủi ro;
  - dùng cho hoạt động không chịu thuế.
- Hàng khuyến mại, biếu tặng, tiêu dùng nội bộ: kiểm tra đã xuất hóa đơn và kê khai đúng.
- Kết quả: số thuế phải nộp hoặc số còn được khấu trừ chuyển kỳ sau.

## 3. Thuế TNCN
- Tổng hợp thu nhập chịu thuế, giảm trừ gia cảnh, số đã khấu trừ, từ bảng lương.
- Thu nhập của lao động thời vụ không ký HĐLĐ: kiểm tra việc khấu trừ 10% và cam kết 08/CK-TNCN (nếu có).

## 4. Thuế TNDN tạm nộp quý
- Ước tính lợi nhuận lũy kế từ đầu năm, loại các chi phí không được trừ đã biết.
- Lưu ý quy định về tổng số tạm nộp 4 quý so với số quyết toán [CẦN KIỂM TRA tỷ lệ hiện hành].

## 5. Quyết toán năm
- Danh mục chi phí không được trừ (xem `kien-thuc/thue-va-phap-ly.md`).
- Hồ sơ hàng hủy, dự phòng, chi phí lãi vay, giao dịch liên kết (nếu có).

## Đầu ra
`bao-cao/<ky>/thue-<loai>.md`, gồm: bảng số liệu theo chỉ tiêu tờ khai, bảng đối chiếu với sổ cái, danh sách hóa đơn bị loại kèm lý do, các điểm [CẦN KIỂM TRA].
