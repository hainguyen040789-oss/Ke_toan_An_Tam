#!/usr/bin/env python3
"""Tính giá thành sản phẩm bánh theo định mức NVL và hệ số quy đổi.

Cách dùng:
    python3 cong-cu/tinh_gia_thanh.py <thu_muc_du_lieu> [--nguong 3] [--loai-vuot-dinh-muc] [--ra file.md]

Thư mục dữ liệu cần 4 file CSV: dinh_muc.csv, san_luong.csv, nvl_xuat.csv,
chi_phi_chung.csv (xem .claude/skills/tinh-gia-thanh/SKILL.md).
"""
import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path


def doc_csv(thu_muc, ten):
    duong_dan = Path(thu_muc) / ten
    if not duong_dan.exists():
        sys.exit(f"Thiếu file {duong_dan}")
    with open(duong_dan, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def so(gia_tri):
    gia_tri = (gia_tri or "").strip().replace(" ", "")
    return float(gia_tri) if gia_tri else 0.0


def dinh_dang(x):
    return f"{round(x):,}".replace(",", ".")


def dinh_dang_sl(x):
    return f"{x:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")


def phan_bo(tong, trong_so):
    """Phân bổ `tong` (làm tròn đồng) theo trọng số; chênh lệch làm tròn dồn vào dòng cuối."""
    tong_ts = sum(trong_so.values())
    if not trong_so or tong_ts == 0:
        return {k: 0 for k in trong_so}
    ket_qua, da_phan_bo = {}, 0
    khoa = list(trong_so)
    for k in khoa[:-1]:
        ket_qua[k] = round(tong * trong_so[k] / tong_ts)
        da_phan_bo += ket_qua[k]
    ket_qua[khoa[-1]] = round(tong) - da_phan_bo
    return ket_qua


def tinh(thu_muc, nguong, loai_vuot):
    dinh_muc = doc_csv(thu_muc, "dinh_muc.csv")
    san_luong = {r["ma_sp"]: r for r in doc_csv(thu_muc, "san_luong.csv")}
    nvl_xuat = doc_csv(thu_muc, "nvl_xuat.csv")
    chi_phi = doc_csv(thu_muc, "chi_phi_chung.csv")
    canh_bao = []

    # Lượng NVL tiêu chuẩn theo từng mã bánh
    tieu_chuan = defaultdict(dict)  # ma_nvl -> {ma_sp: luong}
    for r in dinh_muc:
        sp = r["ma_sp"]
        if sp not in san_luong:
            canh_bao.append(f"Định mức có mã {sp} nhưng không có trong sản lượng, bỏ qua.")
            continue
        tieu_chuan[r["ma_nvl"]][sp] = so(r["dinh_muc"]) * so(san_luong[sp]["sl_hoan_thanh"])

    quy_doi = {sp: so(r["sl_hoan_thanh"]) * so(r.get("he_so") or "1") for sp, r in san_luong.items()}

    nvl_sp = defaultdict(float)
    chenh_lech, tong_vuot = [], 0
    for r in nvl_xuat:
        ma, gia_tri, sl_tt = r["ma_nvl"], so(r["gia_tri"]), so(r["sl_xuat"])
        tc = tieu_chuan.get(ma, {})
        sl_tc = sum(tc.values())
        if sl_tc == 0:
            canh_bao.append(f"NVL {ma} ({r.get('ten_nvl', '')}) không có trong định mức, phân bổ theo sản lượng quy đổi. Cần cập nhật định mức.")
            for sp, v in phan_bo(gia_tri, quy_doi).items():
                nvl_sp[sp] += v
            continue
        ty_le = (sl_tt - sl_tc) / sl_tc * 100
        vuot_sl = max(0.0, sl_tt - sl_tc * (1 + nguong / 100))
        vuot_tien = round(gia_tri * vuot_sl / sl_tt) if sl_tt else 0
        chenh_lech.append((ma, r.get("ten_nvl", ""), sl_tc, sl_tt, ty_le, vuot_tien))
        if loai_vuot and vuot_tien:
            gia_tri -= vuot_tien
            tong_vuot += vuot_tien
        for sp, v in phan_bo(gia_tri, tc).items():
            nvl_sp[sp] += v

    tong_kmuc = defaultdict(float)
    for r in chi_phi:
        km = r["khoan_muc"].strip().upper()
        if km not in ("NCTT", "SXC"):
            canh_bao.append(f"Khoản mục '{r['khoan_muc']}' không hợp lệ (chỉ nhận NCTT/SXC), bỏ qua.")
            continue
        tong_kmuc[km] += so(r["so_tien"])
    nctt = phan_bo(tong_kmuc["NCTT"], quy_doi)
    sxc = phan_bo(tong_kmuc["SXC"], quy_doi)

    dong = []
    for sp, r in san_luong.items():
        dd_dau, dd_cuoi = so(r.get("dd_dau")), so(r.get("dd_cuoi"))
        tong = dd_dau + nvl_sp[sp] + nctt[sp] + sxc[sp] - dd_cuoi
        sl = so(r["sl_hoan_thanh"])
        if sl == 0:
            canh_bao.append(f"Mã {sp} có sản lượng 0, không tính được giá thành đơn vị.")
        dong.append((sp, r.get("ten_sp", ""), sl, dd_dau, nvl_sp[sp], nctt[sp], sxc[sp], dd_cuoi, tong, tong / sl if sl else 0))
    return dong, chenh_lech, tong_vuot, canh_bao, tong_kmuc


def bao_cao(thu_muc, nguong, loai_vuot):
    dong, chenh_lech, tong_vuot, canh_bao, tong_kmuc = tinh(thu_muc, nguong, loai_vuot)
    out = [f"# Bảng tính giá thành – dữ liệu `{thu_muc}`", "",
           "_Bản đề xuất – chờ kế toán trưởng duyệt._", "",
           "| Mã | Tên | SL hoàn thành | DD đầu | NVL TT | NC TT | SXC | DD cuối | Tổng giá thành | Giá đơn vị |",
           "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    tong = [0.0] * 6
    for sp, ten, sl, *so_tien, gdv in dong:
        out.append(f"| {sp} | {ten} | {dinh_dang(sl)} | " + " | ".join(dinh_dang(x) for x in so_tien) + f" | {dinh_dang(gdv)} |")
        tong = [a + b for a, b in zip(tong, so_tien)]
    out.append("| **Cộng** | | | " + " | ".join(f"**{dinh_dang(x)}**" for x in tong) + " | |")

    out += ["", f"## Chênh lệch NVL so với định mức (ngưỡng ±{nguong:g}%)", "",
            "| Mã NVL | Tên | Lượng định mức | Lượng thực tế | Chênh lệch % | Vượt ngưỡng (đ) | Đánh giá |",
            "|---|---|---:|---:|---:|---:|---|"]
    for ma, ten, sl_tc, sl_tt, ty_le, vuot in chenh_lech:
        danh_gia = "⚠ Cần giải trình" if abs(ty_le) > nguong else "Trong ngưỡng"
        out.append(f"| {ma} | {ten} | {dinh_dang_sl(sl_tc)} | {dinh_dang_sl(sl_tt)} | {dinh_dang_sl(ty_le) if ty_le < 0 else '+' + dinh_dang_sl(ty_le)}% | {dinh_dang(vuot)} | {danh_gia} |")

    # Kiểm tra cân đối
    tong_nvl_xuat = sum(so(r["gia_tri"]) for r in doc_csv(thu_muc, "nvl_xuat.csv"))
    ve_phai = tong[0] + tong_nvl_xuat - tong_vuot + tong_kmuc["NCTT"] + tong_kmuc["SXC"] - tong[4]
    lech = round(tong[5] - ve_phai)
    out += ["", "## Kiểm tra cân đối", "",
            f"- DD đầu + NVL xuất − vượt định mức loại ra + NCTT + SXC − DD cuối = {dinh_dang(ve_phai)} đ",
            f"- Tổng giá thành = {dinh_dang(tong[5])} đ → {'✅ Khớp' if lech == 0 else f'❌ Lệch {dinh_dang(lech)} đ'}"]

    out += ["", "## Bút toán đề xuất", "",
            "| TK Nợ | TK Có | Số tiền | Diễn giải |", "|---|---|---:|---|",
            f"| 154 | 621 | {dinh_dang(tong_nvl_xuat)} | Kết chuyển chi phí NVL trực tiếp |",
            f"| 154 | 622 | {dinh_dang(tong_kmuc['NCTT'])} | Kết chuyển chi phí nhân công trực tiếp |",
            f"| 154 | 627 | {dinh_dang(tong_kmuc['SXC'])} | Kết chuyển chi phí sản xuất chung |"]
    if tong_vuot:
        out.append(f"| 632 | 154 | {dinh_dang(tong_vuot)} | NVL vượt định mức không tính vào giá thành |")
    out.append(f"| 155 | 154 | {dinh_dang(tong[5])} | Nhập kho thành phẩm theo giá thành thực tế |")
    out.append("")
    out.append("_Nếu áp dụng TT133: bỏ 3 dòng kết chuyển 621/622/627 vì chi phí đã tập hợp trực tiếp trên 154._")

    if canh_bao:
        out += ["", "## Cảnh báo", ""] + [f"- {c}" for c in canh_bao]
    return "\n".join(out) + "\n"


def main():
    p = argparse.ArgumentParser(description="Tính giá thành sản phẩm bánh")
    p.add_argument("thu_muc", help="Thư mục chứa các file CSV đầu vào")
    p.add_argument("--nguong", type=float, default=3.0, help="Ngưỡng hao hụt NVL cho phép, %% (mặc định 3)")
    p.add_argument("--loai-vuot-dinh-muc", action="store_true", help="Loại phần NVL vượt ngưỡng ra khỏi giá thành (đưa vào 632)")
    p.add_argument("--ra", help="Ghi báo cáo ra file .md thay vì in ra màn hình")
    a = p.parse_args()
    noi_dung = bao_cao(a.thu_muc, a.nguong, a.loai_vuot_dinh_muc)
    if a.ra:
        Path(a.ra).parent.mkdir(parents=True, exist_ok=True)
        Path(a.ra).write_text(noi_dung, encoding="utf-8")
        print(f"Đã ghi {a.ra}")
    else:
        print(noi_dung)


if __name__ == "__main__":
    main()
