---
name: tinh-gia-thanh
description: Tập hợp chi phí và tính giá thành từng loại bánh theo định mức NVL và hệ số quy đổi, kèm phân tích chênh lệch NVL thực tế so với định mức. Dùng khi kế toán trưởng yêu cầu tính giá thành, phân tích giá thành, hoặc kiểm tra hao hụt nguyên liệu.
---

# Tính giá thành sản phẩm bánh

## Dữ liệu đầu vào (CSV UTF-8, mẫu trong `du-lieu/mau/`)

| File | Cột | Ý nghĩa |
|---|---|---|
| `dinh_muc.csv` | `ma_sp, ma_nvl, dinh_muc` | Lượng NVL tiêu chuẩn cho **1 đơn vị** thành phẩm |
| `san_luong.csv` | `ma_sp, ten_sp, sl_hoan_thanh, he_so, dd_dau, dd_cuoi` | Sản lượng nhập kho, hệ số quy đổi (giờ máy / độ phức tạp), giá trị dở dang đầu và cuối kỳ (đồng) |
| `nvl_xuat.csv` | `ma_nvl, ten_nvl, sl_xuat, gia_tri` | NVL thực tế xuất cho sản xuất trong kỳ (đã trừ nhập lại kho) |
| `chi_phi_chung.csv` | `khoan_muc, so_tien` | `khoan_muc` là `NCTT` hoặc `SXC` (có thể có nhiều dòng) |

Nếu kế toán trưởng đưa file Excel hoặc dữ liệu kết xuất từ phần mềm kế toán, chuyển sang các CSV trên trong `du-lieu/<YYYY-MM>/`, không sửa file gốc.

## Phương pháp

1. **NVL trực tiếp:** với mỗi loại NVL, lượng tiêu chuẩn của từng mã bánh = `dinh_muc × sl_hoan_thanh`. Giá trị NVL **thực tế** xuất kho được phân bổ cho các mã bánh theo tỷ lệ lượng tiêu chuẩn đó.
2. **Nhân công trực tiếp và sản xuất chung:** phân bổ theo sản lượng quy đổi = `sl_hoan_thanh × he_so`.
3. **Giá thành:** `dd_dau + NVL + NCTT + SXC − dd_cuoi`; giá thành đơn vị = tổng giá thành / `sl_hoan_thanh`.
4. **Chênh lệch NVL:** lượng thực tế xuất so với tổng lượng tiêu chuẩn của từng NVL. Vượt ngưỡng hao hụt trong `ho-so-cong-ty.md` thì đưa vào danh sách cần giải trình. Phần vượt định mức không được tính vào giá thành: đề xuất kết chuyển vào 632.

## Chạy công cụ

```bash
python3 cong-cu/tinh_gia_thanh.py du-lieu/<YYYY-MM> --nguong 3 --ra bao-cao/<YYYY-MM>/gia-thanh.md
```

Thêm `--loai-vuot-dinh-muc` để loại phần NVL vượt ngưỡng ra khỏi giá thành; công cụ sẽ in số tiền đề xuất hạch toán vào 632.

## Sau khi chạy
- Kiểm tra: tổng giá thành của các mã bánh = tổng dở dang đầu + tổng chi phí − tổng dở dang cuối (− phần vượt định mức, nếu có).
- So sánh giá thành đơn vị với tháng trước; biến động trên ±5% thì tìm nguyên nhân (giá NVL, sản lượng thấp làm SXC/đơn vị tăng, hao hụt).
- Lập bút toán: Nợ 154 / Có 621, 622, 627; Nợ 155 / Có 154; phần vượt định mức: Nợ 632 / Có 154.
- Nếu công ty áp dụng TT133, bỏ bước kết chuyển 621/622/627 (chi phí đã nằm sẵn trên 154).
