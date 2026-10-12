# Nghiệp vụ đặc thù công ty sản xuất bánh

Số hiệu tài khoản dưới đây theo hệ thống tài khoản của TT200 (TT99/2025 giữ phần lớn các tài khoản này). Nếu công ty áp dụng **TT133**, không dùng 621/622/627 mà tập hợp thẳng vào **154** theo khoản mục chi tiết. Agent phải đối chiếu với chế độ ghi trong `ho-so-cong-ty.md` và đánh dấu [CẦN KIỂM TRA] khi một tài khoản không chắc còn tồn tại trong chế độ đang áp dụng.

## 1. Danh mục tài khoản chi tiết gợi ý

| TK | Nội dung | Chi tiết gợi ý |
|---|---|---|
| 152 | Nguyên liệu, vật liệu | 1521 NVL chính (bột mì, đường, bơ, trứng, sữa, nhân); 1522 phụ gia, hương liệu; 1523 bao bì, hộp, khay, tem nhãn; 1524 nhiên liệu (gas, dầu) |
| 153 | Công cụ dụng cụ | Khuôn, khay nướng, dụng cụ inox |
| 154 | Chi phí SXKD dở dang | Theo phân xưởng / dây chuyền |
| 155 | Thành phẩm | Theo mã bánh, theo lô (số lô + hạn sử dụng) |
| 157 | Hàng gửi đi bán | Hàng ký gửi đại lý / siêu thị |
| 621 | Chi phí NVL trực tiếp | Theo phân xưởng, chi tiết mã bánh |
| 622 | Chi phí nhân công trực tiếp | Công nhân đứng máy, đóng gói |
| 627 | Chi phí sản xuất chung | 6271 nhân viên PX; 6272 vật liệu; 6273 CCDC; 6274 khấu hao lò nướng, máy; 6277 điện, nước, gas; 6278 khác (vệ sinh ATTP, kiểm nghiệm) |
| 632 | Giá vốn hàng bán | Bao gồm hao hụt ngoài định mức, chi phí SXC cố định vượt công suất bình thường |
| 511 | Doanh thu | 5112 bán thành phẩm, chi tiết theo kênh |
| 521 | Các khoản giảm trừ doanh thu | Chiết khấu thương mại, hàng bán bị trả lại, giảm giá |
| 641 | Chi phí bán hàng | Vận chuyển lạnh, hỗ trợ trưng bày, khuyến mại, hàng mẫu |
| 642 | Chi phí quản lý DN | |
| 2294 | Dự phòng giảm giá hàng tồn kho | Hàng cận date, bánh mùa vụ tồn sau mùa |

## 2. Bút toán điển hình

**Mua nguyên liệu nhập kho**
- Nợ 152 / Nợ 1331 / Có 331 (hoặc 112)

**Xuất NVL cho sản xuất theo lệnh sản xuất**
- Nợ 621 (chi tiết mã bánh nếu xuất riêng được) / Có 152
- NVL dùng chung cho nhiều loại bánh (ví dụ bột mì xuất theo mẻ): tập hợp cho phân xưởng, phân bổ cho từng mã bánh theo định mức (xem skill `tinh-gia-thanh`).

**Cuối kỳ kết chuyển và nhập kho thành phẩm**
- Nợ 154 / Có 621, 622, 627
- Nợ 155 / Có 154 (giá thành thực tế)

**Hao hụt, bánh hỏng trong sản xuất**
- Trong định mức: nằm trong giá thành, không hạch toán riêng.
- Ngoài định mức: Nợ 632 (hoặc Nợ 1388 nếu bắt bồi thường) / Có 154 (hoặc 152).
- Phế liệu thu hồi bán được (vụn bánh làm thức ăn chăn nuôi…): Nợ 152/111 / Có 154.

**Thành phẩm hết hạn sử dụng, tiêu hủy**
- Lập hội đồng tiêu hủy, biên bản tiêu hủy có chữ ký, ảnh/video, bảng kê lô hàng. Đây là căn cứ để chi phí được trừ khi tính thuế TNDN.
- Nợ 632 / Có 155 (nếu đã trích dự phòng: Nợ 2294 / Có 632 phần hoàn nhập tương ứng).

**Hàng bán bị trả lại (hàng cận date, lỗi)**
- Ghi nhận theo hóa đơn điều chỉnh/hóa đơn trả hàng theo quy định hóa đơn điện tử hiện hành [CẦN KIỂM TRA thủ tục cụ thể].
- Nợ 5212 / Nợ 33311 / Có 131
- Nhập lại kho: Nợ 155 / Có 632; nếu hàng không còn giá trị thì tiếp tục làm thủ tục tiêu hủy.

**Chiết khấu thương mại cho đại lý / siêu thị**
- Trừ ngay trên hóa đơn: ghi doanh thu theo giá đã trừ chiết khấu.
- Chiết khấu theo doanh số, cuối kỳ mới tính: Nợ 5211 / Nợ 33311 / Có 131.
- Phí trưng bày, phí niêm yết do siêu thị xuất hóa đơn: Nợ 641 / Nợ 1331 / Có 331 hoặc trừ công nợ (đối chiếu hợp đồng).

**Hàng khuyến mại, hàng mẫu, biếu tặng**
- Khuyến mại có đăng ký/thông báo theo quy định thương mại: Nợ 641 / Có 155 (theo giá vốn); hóa đơn ghi rõ hàng khuyến mại [CẦN KIỂM TRA cách xác định thuế GTGT theo quy định hiện hành].
- Biếu tặng, tiêu dùng nội bộ: xuất hóa đơn, kê khai thuế GTGT theo giá tính thuế của sản phẩm cùng loại.

**Bánh mùa vụ (Trung thu, Tết)**
- Theo dõi riêng mã sản phẩm và lệnh sản xuất của mùa vụ.
- Chi phí bao bì, hộp quà đặt trước: theo dõi trên 1523, phân bổ vào giá thành theo số hộp thực tế sản xuất.
- Hết mùa: đối chiếu hàng gửi đại lý (157), nhận hàng trả về, lập dự phòng/tiêu hủy phần tồn; đánh giá biên lợi nhuận cả mùa.

## 3. Điểm kiểm soát hay sai

- Định mức NVL không cập nhật khi đổi công thức hoặc đổi nhà cung cấp, làm chênh lệch NVL lớn bất thường.
- Xuất kho NVL không gắn lệnh sản xuất nên không phân bổ được.
- Hàng gửi siêu thị (157) không đối chiếu định kỳ, dẫn đến lệch giữa doanh thu và tồn kho.
- Thiếu biên bản tiêu hủy hàng hết hạn khiến chi phí bị loại khi quyết toán thuế.
- Chi phí điện, gas lớn nhưng không có tiêu thức phân bổ hợp lý giữa các phân xưởng.
- Lao động thời vụ mùa cao điểm: thiếu hợp đồng, không khấu trừ thuế TNCN 10% với thu nhập từ 2 triệu đồng/lần trở lên khi không ký HĐLĐ [CẦN KIỂM TRA ngưỡng hiện hành].
- Bao bì in sẵn nhãn của mùa trước không dùng được nữa nhưng vẫn ghi nhận là tồn kho.
