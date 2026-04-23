import streamlit as st

# 1. Konfigurasi Halaman agar pas di HP
st.set_page_config(
    page_title="Kasir Warung Mas Dwi",
    page_icon="🏪",
    layout="centered"
)

# 2. Judul Aplikasi
st.title("🏪 Kasir warung Imafatih")
st.write("Aplikasi penghitung laba bersih otomatis untuk HP.")

# 3. Input Jumlah Terjual (Layout dibuat 2 kolom agar rapi)
st.subheader("Input Penjualan Hari Ini:")
col1, col2 = st.columns(2)

with col1:
    qty_a = st.number_input("Jajan A (Rp 1.000)", min_value=0, step=1, value=0)
    qty_c = st.number_input("Jajan C (Rp 3.000)", min_value=0, step=1, value=0)

with col2:
    qty_b = st.number_input("Jajan B (Rp 2.000)", min_value=0, step=1, value=0)
    qty_d = st.number_input("Jajan D (Rp 4.000)", min_value=0, step=1, value=0)

# 4. Tombol Hitung
if st.button("HITUNG LABA BERSIH", use_container_width=True):
    # Logika Harga & Modal (Sesuai request Mas Dwi)
    # Jajan A: Jual 1000, Modal 800 -> Untung 200
    untung_a = (1000 - 800) * qty_a
    untung_b = (2000 - 1600) * qty_b
    untung_c = (3000 - 2400) * qty_c
    untung_d = (4000 - 3200) * qty_d
    
    total_omzet = (qty_a * 1000) + (qty_b * 2000) + (qty_c * 3000) + (qty_d * 4000)
    total_laba = untung_a + untung_b + untung_c + untung_d
    
    st.markdown("---")
    
    # 5. Menampilkan Hasil dengan tampilan keren
    st.metric(label="TOTAL UANG MASUK (OMZET)", value=f"Rp {total_omzet:,.0f}")
    st.metric(label="KEUNTUNGAN BERSIH (LABA)", value=f"Rp {total_laba:,.0f}", delta="Sudah dipotong modal")
    
    if total_laba > 0:
        st.success(f"Alhamdulillah, untung bersih hari ini: Rp {total_laba:,.0f}")
    else:
        st.warning("Belum ada data penjualan yang dimasukkan.")

# 6. Catatan kaki
st.caption("Dikembangkan oleh Mas Dwi Prasetyo - Guru Informatika & Teknisi IT")
